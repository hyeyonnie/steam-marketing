import logging
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from database import db
from .data_processor import data_processor

class MetricsCalculator:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def calculate_daily_summary(self, customer_id: str, date: str = None) -> Dict[str, Any]:
        try:
            target_date = date or datetime.now().strftime('%Y-%m-%d')
            
            summary = {
                'date': target_date,
                'customer_id': customer_id,
                'platforms': {},
                'overall_performance': {},
                'growth_metrics': {},
                'engagement_metrics': {},
                'generated_at': datetime.now().isoformat()
            }
            
            # Calculate metrics for each platform
            twitter_metrics = self._calculate_twitter_metrics(customer_id, target_date)
            if twitter_metrics:
                summary['platforms']['twitter'] = twitter_metrics
            
            youtube_metrics = self._calculate_youtube_metrics(customer_id, target_date)
            if youtube_metrics:
                summary['platforms']['youtube'] = youtube_metrics
            
            steam_metrics = self._calculate_steam_metrics(customer_id, target_date)
            if steam_metrics:
                summary['platforms']['steam'] = steam_metrics
            
            # Calculate overall performance
            summary['overall_performance'] = self._calculate_overall_performance(summary['platforms'])
            
            # Calculate growth metrics
            summary['growth_metrics'] = self._calculate_growth_metrics(customer_id, target_date)
            
            # Calculate engagement metrics
            summary['engagement_metrics'] = self._calculate_engagement_metrics(summary['platforms'])
            
            return summary
            
        except Exception as e:
            self.logger.error(f"Error calculating daily summary for {customer_id}: {e}")
            return {}
    
    def calculate_weekly_summary(self, customer_id: str, week_start: str = None) -> Dict[str, Any]:
        try:
            if week_start:
                start_date = datetime.strptime(week_start, '%Y-%m-%d')
            else:
                # Get Monday of current week
                today = datetime.now()
                start_date = today - timedelta(days=today.weekday())
            
            end_date = start_date + timedelta(days=6)
            
            summary = {
                'week_start': start_date.strftime('%Y-%m-%d'),
                'week_end': end_date.strftime('%Y-%m-%d'),
                'customer_id': customer_id,
                'daily_summaries': [],
                'weekly_totals': {},
                'trends': {},
                'generated_at': datetime.now().isoformat()
            }
            
            # Get daily summaries for the week
            current_date = start_date
            while current_date <= end_date:
                daily_summary = self.get_stored_daily_summary(customer_id, current_date.strftime('%Y-%m-%d'))
                if daily_summary:
                    summary['daily_summaries'].append(daily_summary)
                current_date += timedelta(days=1)
            
            # Calculate weekly totals
            summary['weekly_totals'] = self._calculate_weekly_totals(summary['daily_summaries'])
            
            # Calculate trends
            summary['trends'] = self._calculate_weekly_trends(summary['daily_summaries'])
            
            return summary
            
        except Exception as e:
            self.logger.error(f"Error calculating weekly summary for {customer_id}: {e}")
            return {}
    
    def calculate_content_performance(self, customer_id: str, platform: str, days: int = 7) -> Dict[str, Any]:
        try:
            performance = {
                'platform': platform,
                'period_days': days,
                'top_content': [],
                'performance_metrics': {},
                'content_analysis': {},
                'recommendations': []
            }
            
            if platform == 'twitter':
                performance = self._analyze_twitter_content_performance(customer_id, days)
            elif platform == 'youtube':
                performance = self._analyze_youtube_content_performance(customer_id, days)
            
            return performance
            
        except Exception as e:
            self.logger.error(f"Error calculating content performance for {customer_id}: {e}")
            return {}
    
    def calculate_roi_metrics(self, customer_id: str, campaign_data: Dict[str, Any] = None) -> Dict[str, Any]:
        try:
            roi_metrics = {
                'customer_id': customer_id,
                'marketing_effectiveness': {},
                'conversion_metrics': {},
                'cost_analysis': {},
                'recommendations': []
            }
            
            # Get follower growth and engagement data
            growth_data = self._get_growth_data(customer_id, 30)
            
            if growth_data:
                roi_metrics['marketing_effectiveness'] = self._calculate_marketing_effectiveness(growth_data)
            
            # Calculate Steam-specific conversion metrics
            steam_data = self._get_steam_conversion_data(customer_id)
            if steam_data:
                roi_metrics['conversion_metrics'] = steam_data
            
            return roi_metrics
            
        except Exception as e:
            self.logger.error(f"Error calculating ROI metrics for {customer_id}: {e}")
            return {}
    
    def _calculate_twitter_metrics(self, customer_id: str, date: str) -> Dict[str, Any]:
        try:
            with db.get_connection() as conn:
                cursor = conn.cursor()
                
                # Get latest Twitter data for the date
                cursor.execute("""
                    SELECT followers_count, following_count, tweet_count, collected_at
                    FROM twitter_data 
                    WHERE customer_id = ? AND DATE(collected_at) = ?
                    ORDER BY collected_at DESC LIMIT 1
                """, (customer_id, date))
                
                user_result = cursor.fetchone()
                
                # Get tweets for the date
                cursor.execute("""
                    SELECT retweet_count, like_count, reply_count, quote_count
                    FROM twitter_tweets 
                    WHERE customer_id = ? AND DATE(collected_at) = ?
                """, (customer_id, date))
                
                tweet_results = cursor.fetchall()
                
                if not user_result:
                    return {}
                
                user_data = dict(user_result)
                
                # Calculate engagement metrics
                total_engagement = sum(
                    tweet[0] + tweet[1] + tweet[2] + tweet[3] 
                    for tweet in tweet_results
                )
                
                metrics = {
                    'followers_count': user_data['followers_count'],
                    'following_count': user_data['following_count'],
                    'total_tweets': len(tweet_results),
                    'total_engagement': total_engagement,
                    'engagement_rate': round(total_engagement / user_data['followers_count'] * 100, 2) if user_data['followers_count'] > 0 else 0,
                    'last_updated': user_data['collected_at']
                }
                
                return metrics
                
        except Exception as e:
            self.logger.error(f"Error calculating Twitter metrics: {e}")
            return {}
    
    def _calculate_youtube_metrics(self, customer_id: str, date: str) -> Dict[str, Any]:
        try:
            with db.get_connection() as conn:
                cursor = conn.cursor()
                
                # Get latest YouTube data for the date
                cursor.execute("""
                    SELECT subscriber_count, video_count, view_count, collected_at
                    FROM youtube_data 
                    WHERE customer_id = ? AND DATE(collected_at) = ?
                    ORDER BY collected_at DESC LIMIT 1
                """, (customer_id, date))
                
                channel_result = cursor.fetchone()
                
                # Get videos for the date
                cursor.execute("""
                    SELECT view_count, like_count, comment_count
                    FROM youtube_videos 
                    WHERE customer_id = ? AND DATE(collected_at) = ?
                """, (customer_id, date))
                
                video_results = cursor.fetchall()
                
                if not channel_result:
                    return {}
                
                channel_data = dict(channel_result)
                
                # Calculate engagement metrics
                total_views = sum(video[0] for video in video_results)
                total_likes = sum(video[1] for video in video_results)
                total_comments = sum(video[2] for video in video_results)
                
                metrics = {
                    'subscriber_count': channel_data['subscriber_count'],
                    'total_videos': len(video_results),
                    'total_views': total_views,
                    'total_likes': total_likes,
                    'total_comments': total_comments,
                    'engagement_rate': round((total_likes + total_comments) / total_views * 100, 2) if total_views > 0 else 0,
                    'last_updated': channel_data['collected_at']
                }
                
                return metrics
                
        except Exception as e:
            self.logger.error(f"Error calculating YouTube metrics: {e}")
            return {}
    
    def _calculate_steam_metrics(self, customer_id: str, date: str) -> Dict[str, Any]:
        try:
            with db.get_connection() as conn:
                cursor = conn.cursor()
                
                # Get latest Steam data for the date
                cursor.execute("""
                    SELECT app_name, wishlist_count, followers_count, review_score, review_count, collected_at
                    FROM steam_data 
                    WHERE customer_id = ? AND DATE(collected_at) = ?
                    ORDER BY collected_at DESC LIMIT 1
                """, (customer_id, date))
                
                result = cursor.fetchone()
                
                if not result:
                    return {}
                
                data = dict(result)
                
                metrics = {
                    'app_name': data['app_name'],
                    'wishlist_count': data['wishlist_count'],
                    'followers_count': data['followers_count'],
                    'review_score': data['review_score'],
                    'review_count': data['review_count'],
                    'last_updated': data['collected_at']
                }
                
                return metrics
                
        except Exception as e:
            self.logger.error(f"Error calculating Steam metrics: {e}")
            return {}
    
    def _calculate_overall_performance(self, platforms: Dict[str, Any]) -> Dict[str, Any]:
        try:
            total_followers = 0
            total_engagement = 0
            active_platforms = 0
            
            for platform, metrics in platforms.items():
                active_platforms += 1
                
                if platform == 'twitter':
                    total_followers += metrics.get('followers_count', 0)
                    total_engagement += metrics.get('total_engagement', 0)
                elif platform == 'youtube':
                    total_followers += metrics.get('subscriber_count', 0)
                    total_engagement += metrics.get('total_likes', 0) + metrics.get('total_comments', 0)
                elif platform == 'steam':
                    total_followers += metrics.get('wishlist_count', 0) + metrics.get('followers_count', 0)
            
            performance = {
                'total_followers': total_followers,
                'total_engagement': total_engagement,
                'active_platforms': active_platforms,
                'average_engagement_rate': self._calculate_weighted_engagement_rate(platforms)
            }
            
            return performance
            
        except Exception as e:
            self.logger.error(f"Error calculating overall performance: {e}")
            return {}
    
    def _calculate_growth_metrics(self, customer_id: str, date: str) -> Dict[str, Any]:
        try:
            growth_metrics = {}
            
            # Calculate day-over-day growth for each platform
            for platform in ['twitter', 'youtube', 'steam']:
                growth = self._calculate_platform_growth(customer_id, platform, date)
                if growth:
                    growth_metrics[platform] = growth
            
            return growth_metrics
            
        except Exception as e:
            self.logger.error(f"Error calculating growth metrics: {e}")
            return {}
    
    def _calculate_platform_growth(self, customer_id: str, platform: str, date: str) -> Dict[str, Any]:
        try:
            with db.get_connection() as conn:
                cursor = conn.cursor()
                
                if platform == 'twitter':
                    cursor.execute("""
                        SELECT followers_count, collected_at
                        FROM twitter_data 
                        WHERE customer_id = ? AND DATE(collected_at) <= ?
                        ORDER BY collected_at DESC LIMIT 2
                    """, (customer_id, date))
                elif platform == 'youtube':
                    cursor.execute("""
                        SELECT subscriber_count, collected_at
                        FROM youtube_data 
                        WHERE customer_id = ? AND DATE(collected_at) <= ?
                        ORDER BY collected_at DESC LIMIT 2
                    """, (customer_id, date))
                elif platform == 'steam':
                    cursor.execute("""
                        SELECT wishlist_count, collected_at
                        FROM steam_data 
                        WHERE customer_id = ? AND DATE(collected_at) <= ?
                        ORDER BY collected_at DESC LIMIT 2
                    """, (customer_id, date))
                
                results = cursor.fetchall()
                
                if len(results) < 2:
                    return {}
                
                current = results[0][0]
                previous = results[1][0]
                
                growth_absolute = current - previous
                growth_percentage = round((growth_absolute / previous * 100), 2) if previous > 0 else 0
                
                return {
                    'current': current,
                    'previous': previous,
                    'growth_absolute': growth_absolute,
                    'growth_percentage': growth_percentage,
                    'trend': 'up' if growth_absolute > 0 else 'down' if growth_absolute < 0 else 'stable'
                }
                
        except Exception as e:
            self.logger.error(f"Error calculating {platform} growth: {e}")
            return {}
    
    def _calculate_engagement_metrics(self, platforms: Dict[str, Any]) -> Dict[str, Any]:
        try:
            engagement_summary = {
                'best_performing_platform': '',
                'overall_engagement_trend': 'stable',
                'platform_comparison': {}
            }
            
            best_rate = 0
            best_platform = ''
            
            for platform, metrics in platforms.items():
                engagement_rate = metrics.get('engagement_rate', 0)
                
                engagement_summary['platform_comparison'][platform] = {
                    'engagement_rate': engagement_rate,
                    'performance_level': self._categorize_performance(platform, engagement_rate)
                }
                
                if engagement_rate > best_rate:
                    best_rate = engagement_rate
                    best_platform = platform
            
            engagement_summary['best_performing_platform'] = best_platform
            
            return engagement_summary
            
        except Exception as e:
            self.logger.error(f"Error calculating engagement metrics: {e}")
            return {}
    
    def _categorize_performance(self, platform: str, engagement_rate: float) -> str:
        # Platform-specific performance thresholds
        thresholds = {
            'twitter': {'excellent': 3.0, 'good': 1.5, 'average': 0.5},
            'youtube': {'excellent': 8.0, 'good': 4.0, 'average': 2.0},
            'steam': {'excellent': 15.0, 'good': 10.0, 'average': 5.0}
        }
        
        platform_thresholds = thresholds.get(platform, thresholds['twitter'])
        
        if engagement_rate >= platform_thresholds['excellent']:
            return 'excellent'
        elif engagement_rate >= platform_thresholds['good']:
            return 'good'
        elif engagement_rate >= platform_thresholds['average']:
            return 'average'
        else:
            return 'needs_improvement'
    
    def store_daily_summary(self, customer_id: str, summary: Dict[str, Any]) -> bool:
        try:
            date = summary.get('date')
            
            with db.get_connection() as conn:
                cursor = conn.cursor()
                
                # Store summary for each platform
                for platform, metrics in summary.get('platforms', {}).items():
                    cursor.execute("""
                        INSERT OR REPLACE INTO daily_performance 
                        (customer_id, date, platform, metrics)
                        VALUES (?, ?, ?, ?)
                    """, (customer_id, date, platform, json.dumps(metrics)))
                
                conn.commit()
                
            self.logger.info(f"Stored daily summary for {customer_id} on {date}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error storing daily summary: {e}")
            return False
    
    def get_stored_daily_summary(self, customer_id: str, date: str) -> Optional[Dict[str, Any]]:
        try:
            with db.get_connection() as conn:
                cursor = conn.cursor()
                
                cursor.execute("""
                    SELECT platform, metrics FROM daily_performance 
                    WHERE customer_id = ? AND date = ?
                """, (customer_id, date))
                
                results = cursor.fetchall()
                
                if not results:
                    return None
                
                summary = {
                    'date': date,
                    'customer_id': customer_id,
                    'platforms': {}
                }
                
                for platform, metrics_json in results:
                    try:
                        metrics = json.loads(metrics_json)
                        summary['platforms'][platform] = metrics
                    except:
                        continue
                
                return summary
                
        except Exception as e:
            self.logger.error(f"Error getting stored daily summary: {e}")
            return None
    
    def _calculate_weekly_totals(self, daily_summaries: List[Dict[str, Any]]) -> Dict[str, Any]:
        # Implementation for weekly totals calculation
        pass
    
    def _calculate_weekly_trends(self, daily_summaries: List[Dict[str, Any]]) -> Dict[str, Any]:
        # Implementation for weekly trends calculation
        pass
    
    def _calculate_weighted_engagement_rate(self, platforms: Dict[str, Any]) -> float:
        # Implementation for weighted engagement rate calculation
        pass
    
    def _analyze_twitter_content_performance(self, customer_id: str, days: int) -> Dict[str, Any]:
        # Implementation for Twitter content analysis
        pass
    
    def _analyze_youtube_content_performance(self, customer_id: str, days: int) -> Dict[str, Any]:
        # Implementation for YouTube content analysis
        pass
    
    def _get_growth_data(self, customer_id: str, days: int) -> Dict[str, Any]:
        # Implementation for growth data retrieval
        pass
    
    def _calculate_marketing_effectiveness(self, growth_data: Dict[str, Any]) -> Dict[str, Any]:
        # Implementation for marketing effectiveness calculation
        pass
    
    def _get_steam_conversion_data(self, customer_id: str) -> Dict[str, Any]:
        # Implementation for Steam conversion data
        pass

# Global instance
metrics_calculator = MetricsCalculator()