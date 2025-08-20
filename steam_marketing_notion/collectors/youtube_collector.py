import logging
import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from googleapiclient.discovery import build
from google.auth.exceptions import RefreshError
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from config.api_config import api_config
from config.settings import settings
from database import db

class YouTubeCollector:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.rate_limit = api_config.get_rate_limit('youtube')
        self.config = settings.get_data_collection_config().get('youtube', {})
        self.youtube_service = None
        self._initialize_api()
    
    def _initialize_api(self):
        try:
            youtube_config = api_config.get_youtube_config()
            
            if not youtube_config.get('api_key'):
                self.logger.error("YouTube API key not configured")
                return
            
            # Initialize YouTube Data API v3
            self.youtube_service = build(
                'youtube', 
                'v3', 
                developerKey=youtube_config['api_key']
            )
            
            self.logger.info("YouTube API initialized successfully")
            
        except Exception as e:
            self.logger.error(f"Failed to initialize YouTube API: {e}")
    
    def test_connection(self, api_key: str = None) -> bool:
        try:
            test_key = api_key or api_config.get_youtube_config().get('api_key')
            
            if not test_key:
                return False
            
            # Test with a simple API call
            test_service = build('youtube', 'v3', developerKey=test_key)
            
            # Search for a popular video to test API access
            request = test_service.search().list(
                part="snippet",
                q="test",
                maxResults=1,
                type="video"
            )
            response = request.execute()
            
            if 'items' in response:
                self.logger.info("YouTube API connection test successful")
                return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"YouTube API connection test failed: {e}")
            return False
    
    def get_channel_by_id(self, channel_id: str) -> Optional[Dict[str, Any]]:
        try:
            if not self.youtube_service:
                self.logger.error("YouTube API not initialized")
                return None
            
            request = self.youtube_service.channels().list(
                part="snippet,statistics,contentDetails",
                id=channel_id
            )
            response = request.execute()
            
            if response.get('items'):
                channel = response['items'][0]
                return {
                    'id': channel['id'],
                    'snippet': channel['snippet'],
                    'statistics': channel['statistics'],
                    'contentDetails': channel.get('contentDetails', {})
                }
            
            return None
            
        except Exception as e:
            self.logger.error(f"Error getting channel {channel_id}: {e}")
            return None
    
    def get_channel_by_username(self, username: str) -> Optional[Dict[str, Any]]:
        try:
            if not self.youtube_service:
                self.logger.error("YouTube API not initialized")
                return None
            
            request = self.youtube_service.channels().list(
                part="snippet,statistics,contentDetails",
                forUsername=username
            )
            response = request.execute()
            
            if response.get('items'):
                channel = response['items'][0]
                return {
                    'id': channel['id'],
                    'snippet': channel['snippet'],
                    'statistics': channel['statistics'],
                    'contentDetails': channel.get('contentDetails', {})
                }
            
            return None
            
        except Exception as e:
            self.logger.error(f"Error getting channel by username {username}: {e}")
            return None
    
    def get_channel_videos(self, channel_id: str, hours_back: int = 24) -> List[Dict[str, Any]]:
        try:
            if not self.youtube_service:
                self.logger.error("YouTube API not initialized")
                return []
            
            # Calculate start time
            published_after = (datetime.now() - timedelta(hours=hours_back)).isoformat() + 'Z'
            
            # Search for videos from the channel
            search_request = self.youtube_service.search().list(
                part="id,snippet",
                channelId=channel_id,
                publishedAfter=published_after,
                order="date",
                type="video",
                maxResults=50
            )
            search_response = search_request.execute()
            
            video_ids = [item['id']['videoId'] for item in search_response.get('items', [])]
            
            if not video_ids:
                return []
            
            # Get detailed video information
            videos_request = self.youtube_service.videos().list(
                part="snippet,statistics,contentDetails",
                id=','.join(video_ids)
            )
            videos_response = videos_request.execute()
            
            videos = []
            for video in videos_response.get('items', []):
                video_data = {
                    'id': video['id'],
                    'snippet': video['snippet'],
                    'statistics': video['statistics'],
                    'contentDetails': video['contentDetails'],
                    'channel_id': channel_id
                }
                videos.append(video_data)
            
            self.logger.info(f"Retrieved {len(videos)} videos for channel {channel_id}")
            return videos
            
        except Exception as e:
            self.logger.error(f"Error getting videos for channel {channel_id}: {e}")
            return []
    
    def collect_channel_data(self, customer_id: str, channel_id: str) -> bool:
        try:
            # Get channel information
            channel_data = self.get_channel_by_id(channel_id)
            if not channel_data:
                self.logger.error(f"Could not retrieve channel data for {channel_id}")
                return False
            
            # Store channel data
            success = db.store_youtube_data(customer_id, channel_data)
            if not success:
                self.logger.error(f"Failed to store YouTube channel data for {customer_id}")
                return False
            
            # Get and store recent videos
            hours_back = self.config.get('fetch_videos_hours', 24)
            videos = self.get_channel_videos(channel_id, hours_back)
            
            if videos:
                success = self._store_youtube_videos(customer_id, videos)
                if not success:
                    self.logger.error(f"Failed to store YouTube videos for {customer_id}")
                    return False
            
            self.logger.info(f"Successfully collected YouTube data for {customer_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error collecting YouTube data for {customer_id}: {e}")
            return False
    
    def _store_youtube_videos(self, customer_id: str, videos: List[Dict[str, Any]]) -> bool:
        try:
            with db.get_connection() as conn:
                cursor = conn.cursor()
                
                for video in videos:
                    snippet = video.get('snippet', {})
                    statistics = video.get('statistics', {})
                    content_details = video.get('contentDetails', {})
                    
                    cursor.execute("""
                        INSERT OR REPLACE INTO youtube_videos 
                        (customer_id, video_id, channel_id, title, description, 
                         published_at, view_count, like_count, comment_count, duration)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        customer_id,
                        video['id'],
                        video['channel_id'],
                        snippet.get('title'),
                        snippet.get('description'),
                        snippet.get('publishedAt'),
                        int(statistics.get('viewCount', 0)),
                        int(statistics.get('likeCount', 0)),
                        int(statistics.get('commentCount', 0)),
                        content_details.get('duration')
                    ))
                
                conn.commit()
                return True
                
        except Exception as e:
            self.logger.error(f"Error storing YouTube videos for {customer_id}: {e}")
            return False
    
    def collect_all_customers(self) -> Dict[str, bool]:
        results = {}
        customers = db.get_all_customers()
        
        for customer in customers:
            customer_id = customer['customer_id']
            
            # Get YouTube connection info
            connections = db.get_social_connections(customer_id)
            youtube_connection = next((c for c in connections if c['platform'] == 'youtube'), None)
            
            if not youtube_connection or youtube_connection['status'] != 'connected':
                self.logger.warning(f"No active YouTube connection for customer {customer_id}")
                results[customer_id] = False
                continue
            
            try:
                # Parse connection data to get channel ID
                connection_data = json.loads(youtube_connection['connection_data'])
                channel_id = connection_data.get('channel_id')
                
                if not channel_id:
                    self.logger.error(f"No channel ID found for customer {customer_id}")
                    results[customer_id] = False
                    continue
                
                # Collect data
                success = self.collect_channel_data(customer_id, channel_id)
                results[customer_id] = success
                
                # Update processing status
                status = 'completed' if success else 'failed'
                db.update_processing_status(customer_id, 'youtube_collection', status)
                
                # Rate limiting
                time.sleep(0.1)  # YouTube has high rate limits but still be respectful
                
            except Exception as e:
                self.logger.error(f"Error processing customer {customer_id}: {e}")
                results[customer_id] = False
                db.update_processing_status(customer_id, 'youtube_collection', 'failed', str(e))
        
        return results
    
    def validate_connection_data(self, connection_data: Dict[str, str]) -> Dict[str, Any]:
        try:
            channel_id = connection_data.get('channel_id')
            api_key = connection_data.get('api_key')
            
            if not channel_id:
                return {'valid': False, 'error': 'Channel ID is required'}
            
            # Test API key if provided, otherwise use default
            if api_key:
                test_success = self.test_connection(api_key)
                if not test_success:
                    return {'valid': False, 'error': 'Invalid API key'}
            
            # Get channel info to validate
            channel_data = self.get_channel_by_id(channel_id)
            
            if channel_data:
                return {
                    'valid': True,
                    'channel_id': channel_data['id'],
                    'channel_name': channel_data['snippet']['title'],
                    'subscriber_count': channel_data['statistics'].get('subscriberCount', 'Hidden'),
                    'video_count': channel_data['statistics'].get('videoCount', 0)
                }
            
            return {'valid': False, 'error': 'Channel not found or invalid'}
            
        except Exception as e:
            return {'valid': False, 'error': str(e)}
    
    def get_performance_summary(self, customer_id: str, days: int = 7) -> Dict[str, Any]:
        try:
            with db.get_connection() as conn:
                cursor = conn.cursor()
                
                # Get video performance for the last N days
                cursor.execute("""
                    SELECT 
                        COUNT(*) as video_count,
                        SUM(view_count) as total_views,
                        SUM(like_count) as total_likes,
                        SUM(comment_count) as total_comments,
                        AVG(view_count) as avg_views,
                        AVG(like_count) as avg_likes,
                        AVG(comment_count) as avg_comments
                    FROM youtube_videos 
                    WHERE customer_id = ? 
                    AND collected_at >= datetime('now', '-{} days')
                """.format(days), (customer_id,))
                
                result = cursor.fetchone()
                
                # Get latest channel stats
                cursor.execute("""
                    SELECT subscriber_count, video_count, view_count
                    FROM youtube_data 
                    WHERE customer_id = ? 
                    ORDER BY collected_at DESC 
                    LIMIT 1
                """, (customer_id,))
                
                channel_stats = cursor.fetchone()
                
                summary = {
                    'period_days': days,
                    'new_videos': result[0] if result else 0,
                    'total_engagement': {
                        'views': result[1] or 0,
                        'likes': result[2] or 0,
                        'comments': result[3] or 0
                    },
                    'average_engagement': {
                        'views': round(result[4] or 0, 2),
                        'likes': round(result[5] or 0, 2),
                        'comments': round(result[6] or 0, 2)
                    }
                }
                
                if channel_stats:
                    summary['channel_stats'] = {
                        'subscribers': channel_stats[0],
                        'total_videos': channel_stats[1],
                        'total_views': channel_stats[2]
                    }
                
                return summary
                
        except Exception as e:
            self.logger.error(f"Error getting performance summary for {customer_id}: {e}")
            return {}
    
    def search_channel_by_name(self, channel_name: str) -> List[Dict[str, Any]]:
        try:
            if not self.youtube_service:
                self.logger.error("YouTube API not initialized")
                return []
            
            request = self.youtube_service.search().list(
                part="snippet",
                q=channel_name,
                type="channel",
                maxResults=10
            )
            response = request.execute()
            
            channels = []
            for item in response.get('items', []):
                channel_info = {
                    'id': item['id']['channelId'],
                    'title': item['snippet']['title'],
                    'description': item['snippet']['description'],
                    'thumbnail': item['snippet']['thumbnails'].get('default', {}).get('url')
                }
                channels.append(channel_info)
            
            return channels
            
        except Exception as e:
            self.logger.error(f"Error searching for channel {channel_name}: {e}")
            return []

# Global instance
youtube_collector = YouTubeCollector()