import logging
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from database import db

class DataProcessor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def clean_twitter_data(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            cleaned = {
                'user_id': raw_data.get('id'),
                'username': raw_data.get('username', '').lower().strip(),
                'display_name': raw_data.get('name', '').strip(),
                'description': self._clean_text(raw_data.get('description', '')),
                'verified': bool(raw_data.get('verified', False)),
                'created_at': self._parse_datetime(raw_data.get('created_at')),
                'metrics': {
                    'followers': int(raw_data.get('public_metrics', {}).get('followers_count', 0)),
                    'following': int(raw_data.get('public_metrics', {}).get('following_count', 0)),
                    'tweets': int(raw_data.get('public_metrics', {}).get('tweet_count', 0)),
                    'listed': int(raw_data.get('public_metrics', {}).get('listed_count', 0))
                }
            }
            
            return cleaned
            
        except Exception as e:
            self.logger.error(f"Error cleaning Twitter data: {e}")
            return {}
    
    def clean_youtube_data(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            statistics = raw_data.get('statistics', {})
            snippet = raw_data.get('snippet', {})
            
            cleaned = {
                'channel_id': raw_data.get('id'),
                'channel_name': snippet.get('title', '').strip(),
                'description': self._clean_text(snippet.get('description', '')),
                'created_at': self._parse_datetime(snippet.get('publishedAt')),
                'country': snippet.get('country', ''),
                'metrics': {
                    'subscribers': int(statistics.get('subscriberCount', 0)),
                    'videos': int(statistics.get('videoCount', 0)),
                    'views': int(statistics.get('viewCount', 0))
                },
                'custom_url': snippet.get('customUrl', ''),
                'thumbnails': snippet.get('thumbnails', {})
            }
            
            return cleaned
            
        except Exception as e:
            self.logger.error(f"Error cleaning YouTube data: {e}")
            return {}
    
    def clean_steam_data(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        try:
            cleaned = {
                'app_id': int(raw_data.get('steam_appid', 0)),
                'name': raw_data.get('name', '').strip(),
                'type': raw_data.get('type', 'game'),
                'is_free': bool(raw_data.get('is_free', False)),
                'developers': raw_data.get('developers', []),
                'publishers': raw_data.get('publishers', []),
                'categories': [cat.get('description', '') for cat in raw_data.get('categories', [])],
                'genres': [genre.get('description', '') for genre in raw_data.get('genres', [])],
                'release_date': self._parse_steam_date(raw_data.get('release_date', {})),
                'metrics': {
                    'wishlist_count': int(raw_data.get('wishlist_count', 0)),
                    'followers_count': int(raw_data.get('followers_count', 0)),
                    'review_score': float(raw_data.get('review_score', 0)),
                    'review_count': int(raw_data.get('review_count', 0)),
                    'owners': raw_data.get('owners', '0 .. 0'),
                    'players_2weeks': int(raw_data.get('players_2weeks', 0)),
                    'average_playtime': int(raw_data.get('average_playtime', 0))
                }
            }
            
            return cleaned
            
        except Exception as e:
            self.logger.error(f"Error cleaning Steam data: {e}")
            return {}
    
    def process_tweet_engagement(self, tweets: List[Dict[str, Any]]) -> Dict[str, Any]:
        try:
            if not tweets:
                return {}
            
            total_tweets = len(tweets)
            total_retweets = sum(tweet.get('public_metrics', {}).get('retweet_count', 0) for tweet in tweets)
            total_likes = sum(tweet.get('public_metrics', {}).get('like_count', 0) for tweet in tweets)
            total_replies = sum(tweet.get('public_metrics', {}).get('reply_count', 0) for tweet in tweets)
            total_quotes = sum(tweet.get('public_metrics', {}).get('quote_count', 0) for tweet in tweets)
            
            engagement_summary = {
                'total_tweets': total_tweets,
                'total_engagement': {
                    'retweets': total_retweets,
                    'likes': total_likes,
                    'replies': total_replies,
                    'quotes': total_quotes,
                    'total': total_retweets + total_likes + total_replies + total_quotes
                },
                'average_engagement': {
                    'retweets': round(total_retweets / total_tweets, 2) if total_tweets > 0 else 0,
                    'likes': round(total_likes / total_tweets, 2) if total_tweets > 0 else 0,
                    'replies': round(total_replies / total_tweets, 2) if total_tweets > 0 else 0,
                    'quotes': round(total_quotes / total_tweets, 2) if total_tweets > 0 else 0
                },
                'engagement_rate': round((total_retweets + total_likes + total_replies + total_quotes) / total_tweets, 2) if total_tweets > 0 else 0,
                'top_performing_tweet': self._find_top_tweet(tweets),
                'tweet_frequency': self._calculate_tweet_frequency(tweets)
            }
            
            return engagement_summary
            
        except Exception as e:
            self.logger.error(f"Error processing tweet engagement: {e}")
            return {}
    
    def process_youtube_performance(self, videos: List[Dict[str, Any]]) -> Dict[str, Any]:
        try:
            if not videos:
                return {}
            
            total_videos = len(videos)
            total_views = sum(int(video.get('statistics', {}).get('viewCount', 0)) for video in videos)
            total_likes = sum(int(video.get('statistics', {}).get('likeCount', 0)) for video in videos)
            total_comments = sum(int(video.get('statistics', {}).get('commentCount', 0)) for video in videos)
            
            performance_summary = {
                'total_videos': total_videos,
                'total_performance': {
                    'views': total_views,
                    'likes': total_likes,
                    'comments': total_comments
                },
                'average_performance': {
                    'views': round(total_views / total_videos, 2) if total_videos > 0 else 0,
                    'likes': round(total_likes / total_videos, 2) if total_videos > 0 else 0,
                    'comments': round(total_comments / total_videos, 2) if total_videos > 0 else 0
                },
                'engagement_rate': round((total_likes + total_comments) / total_views * 100, 2) if total_views > 0 else 0,
                'top_performing_video': self._find_top_video(videos),
                'upload_frequency': self._calculate_upload_frequency(videos),
                'content_analysis': self._analyze_video_content(videos)
            }
            
            return performance_summary
            
        except Exception as e:
            self.logger.error(f"Error processing YouTube performance: {e}")
            return {}
    
    def normalize_metrics(self, platform: str, raw_metrics: Dict[str, Any]) -> Dict[str, Any]:
        try:
            if platform == 'twitter':
                return {
                    'followers': raw_metrics.get('followers', 0),
                    'engagement_rate': raw_metrics.get('engagement_rate', 0),
                    'content_count': raw_metrics.get('total_tweets', 0),
                    'avg_engagement': raw_metrics.get('average_engagement', {}).get('likes', 0)
                }
            elif platform == 'youtube':
                return {
                    'subscribers': raw_metrics.get('subscribers', 0),
                    'engagement_rate': raw_metrics.get('engagement_rate', 0),
                    'content_count': raw_metrics.get('total_videos', 0),
                    'avg_views': raw_metrics.get('average_performance', {}).get('views', 0)
                }
            elif platform == 'steam':
                return {
                    'wishlist_count': raw_metrics.get('wishlist_count', 0),
                    'followers_count': raw_metrics.get('followers_count', 0),
                    'review_score': raw_metrics.get('review_score', 0),
                    'review_count': raw_metrics.get('review_count', 0)
                }
            
            return raw_metrics
            
        except Exception as e:
            self.logger.error(f"Error normalizing {platform} metrics: {e}")
            return {}
    
    def detect_anomalies(self, customer_id: str, platform: str, current_metrics: Dict[str, Any]) -> List[Dict[str, Any]]:
        try:
            anomalies = []
            
            # Get historical data for comparison
            historical_data = self._get_historical_metrics(customer_id, platform, days=30)
            
            if not historical_data:
                return anomalies
            
            # Check for significant changes
            for metric, current_value in current_metrics.items():
                if not isinstance(current_value, (int, float)):
                    continue
                
                historical_values = [data.get(metric, 0) for data in historical_data]
                if not historical_values:
                    continue
                
                avg_historical = sum(historical_values) / len(historical_values)
                
                # Detect significant increases or decreases (>50% change)
                if avg_historical > 0:
                    change_percent = ((current_value - avg_historical) / avg_historical) * 100
                    
                    if abs(change_percent) > 50:
                        anomaly = {
                            'metric': metric,
                            'current_value': current_value,
                            'historical_average': round(avg_historical, 2),
                            'change_percent': round(change_percent, 2),
                            'type': 'increase' if change_percent > 0 else 'decrease',
                            'severity': 'high' if abs(change_percent) > 100 else 'medium',
                            'detected_at': datetime.now().isoformat()
                        }
                        anomalies.append(anomaly)
            
            return anomalies
            
        except Exception as e:
            self.logger.error(f"Error detecting anomalies for {customer_id}: {e}")
            return []
    
    def _clean_text(self, text: str) -> str:
        if not text:
            return ""
        
        # Remove extra whitespace and newlines
        cleaned = ' '.join(text.split())
        
        # Limit length
        if len(cleaned) > 1000:
            cleaned = cleaned[:997] + "..."
        
        return cleaned
    
    def _parse_datetime(self, date_str: str) -> Optional[str]:
        if not date_str:
            return None
        
        try:
            # Try parsing ISO format
            if 'T' in date_str:
                dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                return dt.isoformat()
            
            return date_str
            
        except:
            return None
    
    def _parse_steam_date(self, date_info: Dict[str, Any]) -> Optional[str]:
        try:
            if date_info.get('coming_soon', False):
                return date_info.get('date', 'Coming Soon')
            
            return date_info.get('date')
            
        except:
            return None
    
    def _find_top_tweet(self, tweets: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not tweets:
            return {}
        
        # Find tweet with highest total engagement
        top_tweet = max(tweets, key=lambda t: (
            t.get('public_metrics', {}).get('retweet_count', 0) +
            t.get('public_metrics', {}).get('like_count', 0) +
            t.get('public_metrics', {}).get('reply_count', 0) +
            t.get('public_metrics', {}).get('quote_count', 0)
        ))
        
        return {
            'id': top_tweet.get('id'),
            'text': top_tweet.get('text', '')[:100] + '...' if len(top_tweet.get('text', '')) > 100 else top_tweet.get('text', ''),
            'total_engagement': (
                top_tweet.get('public_metrics', {}).get('retweet_count', 0) +
                top_tweet.get('public_metrics', {}).get('like_count', 0) +
                top_tweet.get('public_metrics', {}).get('reply_count', 0) +
                top_tweet.get('public_metrics', {}).get('quote_count', 0)
            ),
            'created_at': top_tweet.get('created_at')
        }
    
    def _find_top_video(self, videos: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not videos:
            return {}
        
        # Find video with highest view count
        top_video = max(videos, key=lambda v: int(v.get('statistics', {}).get('viewCount', 0)))
        
        return {
            'id': top_video.get('id'),
            'title': top_video.get('snippet', {}).get('title', ''),
            'views': int(top_video.get('statistics', {}).get('viewCount', 0)),
            'likes': int(top_video.get('statistics', {}).get('likeCount', 0)),
            'comments': int(top_video.get('statistics', {}).get('commentCount', 0)),
            'published_at': top_video.get('snippet', {}).get('publishedAt')
        }
    
    def _calculate_tweet_frequency(self, tweets: List[Dict[str, Any]]) -> str:
        if not tweets:
            return "No tweets"
        
        # Calculate based on creation dates
        dates = []
        for tweet in tweets:
            created_at = tweet.get('created_at')
            if created_at:
                try:
                    dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                    dates.append(dt)
                except:
                    continue
        
        if len(dates) < 2:
            return "Insufficient data"
        
        dates.sort()
        time_span = (dates[-1] - dates[0]).total_seconds() / 3600  # hours
        
        if time_span > 0:
            frequency = len(tweets) / time_span * 24  # tweets per day
            return f"{frequency:.1f} tweets/day"
        
        return "Unknown frequency"
    
    def _calculate_upload_frequency(self, videos: List[Dict[str, Any]]) -> str:
        if not videos:
            return "No videos"
        
        # Calculate based on publication dates
        dates = []
        for video in videos:
            published_at = video.get('snippet', {}).get('publishedAt')
            if published_at:
                try:
                    dt = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
                    dates.append(dt)
                except:
                    continue
        
        if len(dates) < 2:
            return "Insufficient data"
        
        dates.sort()
        time_span = (dates[-1] - dates[0]).total_seconds() / (3600 * 24)  # days
        
        if time_span > 0:
            frequency = len(videos) / time_span
            if frequency >= 1:
                return f"{frequency:.1f} videos/day"
            else:
                return f"{frequency * 7:.1f} videos/week"
        
        return "Unknown frequency"
    
    def _analyze_video_content(self, videos: List[Dict[str, Any]]) -> Dict[str, Any]:
        try:
            durations = []
            categories = {}
            
            for video in videos:
                # Analyze duration if available
                duration = video.get('contentDetails', {}).get('duration')
                if duration:
                    # Parse ISO 8601 duration (PT4M13S -> 253 seconds)
                    seconds = self._parse_duration(duration)
                    if seconds:
                        durations.append(seconds)
                
                # Analyze title keywords
                title = video.get('snippet', {}).get('title', '').lower()
                for keyword in ['trailer', 'gameplay', 'review', 'tutorial', 'update', 'announcement']:
                    if keyword in title:
                        categories[keyword] = categories.get(keyword, 0) + 1
            
            analysis = {
                'total_videos': len(videos),
                'average_duration': round(sum(durations) / len(durations), 0) if durations else 0,
                'content_categories': categories,
                'duration_range': f"{min(durations)//60}m - {max(durations)//60}m" if durations else "Unknown"
            }
            
            return analysis
            
        except Exception as e:
            self.logger.error(f"Error analyzing video content: {e}")
            return {}
    
    def _parse_duration(self, duration: str) -> Optional[int]:
        try:
            # Parse ISO 8601 duration (PT4M13S)
            import re
            pattern = r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?'
            match = re.match(pattern, duration)
            
            if match:
                hours = int(match.group(1) or 0)
                minutes = int(match.group(2) or 0)
                seconds = int(match.group(3) or 0)
                
                return hours * 3600 + minutes * 60 + seconds
            
            return None
            
        except:
            return None
    
    def _get_historical_metrics(self, customer_id: str, platform: str, days: int = 30) -> List[Dict[str, Any]]:
        try:
            with db.get_connection() as conn:
                cursor = conn.cursor()
                
                # Get historical daily performance data
                cursor.execute("""
                    SELECT metrics FROM daily_performance 
                    WHERE customer_id = ? AND platform = ? 
                    AND created_at >= datetime('now', '-{} days')
                    ORDER BY created_at ASC
                """.format(days), (customer_id, platform))
                
                results = cursor.fetchall()
                
                historical_data = []
                for result in results:
                    try:
                        metrics = json.loads(result[0])
                        historical_data.append(metrics)
                    except:
                        continue
                
                return historical_data
                
        except Exception as e:
            self.logger.error(f"Error getting historical metrics: {e}")
            return []

# Global instance
data_processor = DataProcessor()