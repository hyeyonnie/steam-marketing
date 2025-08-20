import tweepy
import logging
import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from config.api_config import api_config
from config.settings import settings
from database import db

class TwitterCollector:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.rate_limit = api_config.get_rate_limit('twitter')
        self.config = settings.get_data_collection_config().get('twitter', {})
        self.api_v2 = None
        self.api_v1 = None
        self._initialize_api()
    
    def _initialize_api(self):
        try:
            twitter_config = api_config.get_twitter_config()
            
            if not all(twitter_config.values()):
                self.logger.error("Twitter API credentials not configured")
                return
            
            # Initialize Twitter API v2 client
            self.api_v2 = tweepy.Client(
                bearer_token=None,
                consumer_key=twitter_config['api_key'],
                consumer_secret=twitter_config['api_secret'],
                access_token=twitter_config['access_token'],
                access_token_secret=twitter_config['access_token_secret'],
                wait_on_rate_limit=True
            )
            
            # Initialize Twitter API v1.1 for additional features
            auth = tweepy.OAuth1UserHandler(
                twitter_config['api_key'],
                twitter_config['api_secret'],
                twitter_config['access_token'],
                twitter_config['access_token_secret']
            )
            self.api_v1 = tweepy.API(auth, wait_on_rate_limit=True)
            
            self.logger.info("Twitter API initialized successfully")
            
        except Exception as e:
            self.logger.error(f"Failed to initialize Twitter API: {e}")
    
    def test_connection(self, credentials: Dict[str, str] = None) -> bool:
        try:
            if credentials:
                # Test with provided credentials
                test_client = tweepy.Client(
                    consumer_key=credentials.get('api_key'),
                    consumer_secret=credentials.get('api_secret'),
                    access_token=credentials.get('access_token'),
                    access_token_secret=credentials.get('access_token_secret'),
                    wait_on_rate_limit=True
                )
                me = test_client.get_me()
            else:
                # Test with current API
                if not self.api_v2:
                    return False
                me = self.api_v2.get_me()
            
            if me.data:
                self.logger.info("Twitter API connection test successful")
                return True
            return False
            
        except Exception as e:
            self.logger.error(f"Twitter API connection test failed: {e}")
            return False
    
    def get_user_by_username(self, username: str) -> Optional[Dict[str, Any]]:
        try:
            if not self.api_v2:
                self.logger.error("Twitter API not initialized")
                return None
            
            user = self.api_v2.get_user(
                username=username,
                user_fields=['public_metrics', 'created_at', 'description', 'verified']
            )
            
            if user.data:
                return {
                    'id': user.data.id,
                    'username': user.data.username,
                    'name': user.data.name,
                    'description': user.data.description,
                    'verified': user.data.verified,
                    'created_at': user.data.created_at,
                    'public_metrics': user.data.public_metrics
                }
            
            return None
            
        except Exception as e:
            self.logger.error(f"Error getting user {username}: {e}")
            return None
    
    def get_user_tweets(self, user_id: str, hours_back: int = 24) -> List[Dict[str, Any]]:
        try:
            if not self.api_v2:
                self.logger.error("Twitter API not initialized")
                return []
            
            # Calculate start time
            start_time = datetime.now() - timedelta(hours=hours_back)
            
            tweets = tweepy.Paginator(
                self.api_v2.get_users_tweets,
                id=user_id,
                start_time=start_time,
                tweet_fields=['public_metrics', 'created_at', 'context_annotations', 'referenced_tweets'],
                max_results=100,
                limit=5  # Limit pages to avoid rate limits
            ).flatten(limit=500)
            
            tweet_list = []
            for tweet in tweets:
                # Skip retweets and replies if configured
                if not self.config.get('include_retweets', False) and hasattr(tweet, 'referenced_tweets'):
                    if any(ref.type == 'retweeted' for ref in tweet.referenced_tweets or []):
                        continue
                
                if not self.config.get('include_replies', False) and tweet.text.startswith('@'):
                    continue
                
                tweet_data = {
                    'id': tweet.id,
                    'text': tweet.text,
                    'created_at': tweet.created_at,
                    'author_id': user_id,
                    'public_metrics': tweet.public_metrics,
                    'context_annotations': getattr(tweet, 'context_annotations', []),
                    'referenced_tweets': getattr(tweet, 'referenced_tweets', [])
                }
                tweet_list.append(tweet_data)
            
            self.logger.info(f"Retrieved {len(tweet_list)} tweets for user {user_id}")
            return tweet_list
            
        except Exception as e:
            self.logger.error(f"Error getting tweets for user {user_id}: {e}")
            return []
    
    def collect_user_data(self, customer_id: str, username: str) -> bool:
        try:
            # Get user information
            user_data = self.get_user_by_username(username)
            if not user_data:
                self.logger.error(f"Could not retrieve user data for {username}")
                return False
            
            # Store user data
            success = db.store_twitter_data(customer_id, user_data)
            if not success:
                self.logger.error(f"Failed to store Twitter user data for {customer_id}")
                return False
            
            # Get and store recent tweets
            user_id = user_data['id']
            hours_back = self.config.get('fetch_tweets_hours', 24)
            tweets = self.get_user_tweets(user_id, hours_back)
            
            if tweets:
                success = db.store_twitter_tweets(customer_id, tweets)
                if not success:
                    self.logger.error(f"Failed to store Twitter tweets for {customer_id}")
                    return False
            
            self.logger.info(f"Successfully collected Twitter data for {customer_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error collecting Twitter data for {customer_id}: {e}")
            return False
    
    def collect_all_customers(self) -> Dict[str, bool]:
        results = {}
        customers = db.get_all_customers()
        
        for customer in customers:
            customer_id = customer['customer_id']
            
            # Get Twitter connection info
            connections = db.get_social_connections(customer_id)
            twitter_connection = next((c for c in connections if c['platform'] == 'twitter'), None)
            
            if not twitter_connection or twitter_connection['status'] != 'connected':
                self.logger.warning(f"No active Twitter connection for customer {customer_id}")
                results[customer_id] = False
                continue
            
            try:
                # Parse connection data to get username
                connection_data = json.loads(twitter_connection['connection_data'])
                username = connection_data.get('username')
                
                if not username:
                    self.logger.error(f"No username found for customer {customer_id}")
                    results[customer_id] = False
                    continue
                
                # Collect data
                success = self.collect_user_data(customer_id, username)
                results[customer_id] = success
                
                # Update processing status
                status = 'completed' if success else 'failed'
                db.update_processing_status(customer_id, 'twitter_collection', status)
                
                # Rate limiting
                time.sleep(1)  # Basic rate limiting
                
            except Exception as e:
                self.logger.error(f"Error processing customer {customer_id}: {e}")
                results[customer_id] = False
                db.update_processing_status(customer_id, 'twitter_collection', 'failed', str(e))
        
        return results
    
    def validate_connection_data(self, connection_data: Dict[str, str]) -> Dict[str, Any]:
        try:
            # Test connection with provided credentials
            test_success = self.test_connection(connection_data)
            
            if test_success:
                # Get user info to validate
                temp_client = tweepy.Client(
                    consumer_key=connection_data.get('api_key'),
                    consumer_secret=connection_data.get('api_secret'),
                    access_token=connection_data.get('access_token'),
                    access_token_secret=connection_data.get('access_token_secret')
                )
                
                me = temp_client.get_me()
                if me.data:
                    return {
                        'valid': True,
                        'username': me.data.username,
                        'user_id': me.data.id,
                        'name': me.data.name
                    }
            
            return {'valid': False, 'error': 'Authentication failed'}
            
        except Exception as e:
            return {'valid': False, 'error': str(e)}
    
    def get_engagement_summary(self, customer_id: str, days: int = 7) -> Dict[str, Any]:
        try:
            with db.get_connection() as conn:
                cursor = conn.cursor()
                
                # Get tweet engagement for the last N days
                cursor.execute("""
                    SELECT 
                        COUNT(*) as tweet_count,
                        SUM(retweet_count) as total_retweets,
                        SUM(like_count) as total_likes,
                        SUM(reply_count) as total_replies,
                        AVG(retweet_count) as avg_retweets,
                        AVG(like_count) as avg_likes,
                        AVG(reply_count) as avg_replies
                    FROM twitter_tweets 
                    WHERE customer_id = ? 
                    AND collected_at >= datetime('now', '-{} days')
                """.format(days), (customer_id,))
                
                result = cursor.fetchone()
                
                if result:
                    return {
                        'period_days': days,
                        'tweet_count': result[0] or 0,
                        'total_engagement': {
                            'retweets': result[1] or 0,
                            'likes': result[2] or 0,
                            'replies': result[3] or 0
                        },
                        'average_engagement': {
                            'retweets': round(result[4] or 0, 2),
                            'likes': round(result[5] or 0, 2),
                            'replies': round(result[6] or 0, 2)
                        }
                    }
                
                return {}
                
        except Exception as e:
            self.logger.error(f"Error getting engagement summary for {customer_id}: {e}")
            return {}

# Global instance
twitter_collector = TwitterCollector()