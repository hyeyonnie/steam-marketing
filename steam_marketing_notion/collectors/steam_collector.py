import requests
import logging
import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from config.api_config import api_config
from config.settings import settings
from database import db

class SteamCollector:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.rate_limit = api_config.get_rate_limit('steam')
        self.config = settings.get_data_collection_config().get('steam', {})
        self.endpoints = api_config.get_endpoints()['steam']
        self.session = requests.Session()
        self.api_key = api_config.get_steam_config().get('api_key')
        
        if not self.api_key:
            self.logger.error("Steam API key not configured")
    
    def test_connection(self, api_key: str = None) -> bool:
        try:
            test_key = api_key or self.api_key
            
            if not test_key:
                return False
            
            # Test with Steam Web API - get Steam user info (using a known Steam ID)
            test_url = f"{self.endpoints['base_url']}/ISteamUser/GetPlayerSummaries/v0002/"
            params = {
                'key': test_key,
                'steamids': '76561197960434622'  # Gabe Newell's public Steam ID for testing
            }
            
            response = self.session.get(test_url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if 'response' in data and 'players' in data['response']:
                    self.logger.info("Steam API connection test successful")
                    return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"Steam API connection test failed: {e}")
            return False
    
    def get_app_details(self, app_id: int) -> Optional[Dict[str, Any]]:
        try:
            url = f"https://store.steampowered.com/api/appdetails"
            params = {
                'appids': app_id,
                'filters': 'basic'
            }
            
            response = self.session.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                app_data = data.get(str(app_id))
                
                if app_data and app_data.get('success') and app_data.get('data'):
                    return app_data['data']
            
            return None
            
        except Exception as e:
            self.logger.error(f"Error getting app details for {app_id}: {e}")
            return None
    
    def get_app_reviews(self, app_id: int, limit: int = 100) -> Dict[str, Any]:
        try:
            url = f"https://store.steampowered.com/appreviews/{app_id}"
            params = {
                'json': 1,
                'filter': 'recent',
                'language': 'english',
                'num_per_page': min(limit, 100)
            }
            
            response = self.session.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'query_summary': data.get('query_summary', {}),
                    'reviews': data.get('reviews', [])
                }
            
            return {}
            
        except Exception as e:
            self.logger.error(f"Error getting app reviews for {app_id}: {e}")
            return {}
    
    def get_app_achievements(self, app_id: int) -> List[Dict[str, Any]]:
        try:
            if not self.api_key:
                return []
            
            url = f"{self.endpoints['base_url']}/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/"
            params = {
                'gameid': app_id,
                'format': 'json'
            }
            
            response = self.session.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                achievements = data.get('achievementpercentages', {}).get('achievements', [])
                return achievements
            
            return []
            
        except Exception as e:
            self.logger.error(f"Error getting achievements for app {app_id}: {e}")
            return []
    
    def get_steam_spy_data(self, app_id: int) -> Optional[Dict[str, Any]]:
        try:
            # SteamSpy API for additional metrics (free but limited)
            url = f"https://steamspy.com/api.php"
            params = {
                'request': 'appdetails',
                'appid': app_id
            }
            
            response = self.session.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data and 'appid' in data:
                    return data
            
            return None
            
        except Exception as e:
            self.logger.error(f"Error getting SteamSpy data for {app_id}: {e}")
            return None
    
    def collect_app_data(self, customer_id: str, app_id: int) -> bool:
        try:
            # Get basic app details
            app_details = self.get_app_details(app_id)
            if not app_details:
                self.logger.error(f"Could not retrieve app details for {app_id}")
                return False
            
            # Get review data
            review_data = self.get_app_reviews(app_id)
            
            # Get SteamSpy data for additional metrics
            steamspy_data = self.get_steam_spy_data(app_id)
            
            # Combine data
            combined_data = {
                'steam_appid': app_id,
                'name': app_details.get('name'),
                'type': app_details.get('type'),
                'is_free': app_details.get('is_free', False),
                'developers': app_details.get('developers', []),
                'publishers': app_details.get('publishers', []),
                'categories': app_details.get('categories', []),
                'genres': app_details.get('genres', []),
                'release_date': app_details.get('release_date', {}),
                'review_score': 0,
                'review_count': 0,
                'followers_count': 0,
                'wishlist_count': 0
            }
            
            # Process review data
            if review_data and 'query_summary' in review_data:
                query_summary = review_data['query_summary']
                combined_data.update({
                    'review_score': query_summary.get('review_score', 0),
                    'review_count': query_summary.get('total_reviews', 0)
                })
            
            # Process SteamSpy data
            if steamspy_data:
                combined_data.update({
                    'followers_count': steamspy_data.get('followers', 0),
                    'owners': steamspy_data.get('owners', '0 .. 0'),
                    'players_forever': steamspy_data.get('players_forever', 0),
                    'players_2weeks': steamspy_data.get('players_2weeks', 0),
                    'average_playtime': steamspy_data.get('average_forever', 0),
                    'median_playtime': steamspy_data.get('median_forever', 0)
                })
            
            # Store data
            success = db.store_steam_data(customer_id, combined_data)
            if not success:
                self.logger.error(f"Failed to store Steam data for {customer_id}")
                return False
            
            self.logger.info(f"Successfully collected Steam data for app {app_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error collecting Steam data for {customer_id}: {e}")
            return False
    
    def collect_all_customers(self) -> Dict[str, bool]:
        results = {}
        customers = db.get_all_customers()
        
        for customer in customers:
            customer_id = customer['customer_id']
            
            # Get Steam connection info
            connections = db.get_social_connections(customer_id)
            steam_connection = next((c for c in connections if c['platform'] == 'steam'), None)
            
            if not steam_connection or steam_connection['status'] != 'connected':
                self.logger.warning(f"No active Steam connection for customer {customer_id}")
                results[customer_id] = False
                continue
            
            try:
                # Parse connection data to get app ID
                connection_data = json.loads(steam_connection['connection_data'])
                app_id = connection_data.get('app_id')
                
                if not app_id:
                    self.logger.error(f"No app ID found for customer {customer_id}")
                    results[customer_id] = False
                    continue
                
                # Collect data
                success = self.collect_app_data(customer_id, int(app_id))
                results[customer_id] = success
                
                # Update processing status
                status = 'completed' if success else 'failed'
                db.update_processing_status(customer_id, 'steam_collection', status)
                
                # Rate limiting (Steam has stricter limits)
                time.sleep(2)
                
            except Exception as e:
                self.logger.error(f"Error processing customer {customer_id}: {e}")
                results[customer_id] = False
                db.update_processing_status(customer_id, 'steam_collection', 'failed', str(e))
        
        return results
    
    def validate_connection_data(self, connection_data: Dict[str, str]) -> Dict[str, Any]:
        try:
            app_id = connection_data.get('app_id')
            api_key = connection_data.get('api_key')
            
            if not app_id:
                return {'valid': False, 'error': 'App ID is required'}
            
            try:
                app_id = int(app_id)
            except ValueError:
                return {'valid': False, 'error': 'App ID must be a number'}
            
            # Test API key if provided
            if api_key:
                test_success = self.test_connection(api_key)
                if not test_success:
                    return {'valid': False, 'error': 'Invalid Steam API key'}
            
            # Get app details to validate
            app_details = self.get_app_details(app_id)
            
            if app_details:
                return {
                    'valid': True,
                    'app_id': app_id,
                    'app_name': app_details.get('name'),
                    'app_type': app_details.get('type'),
                    'developers': app_details.get('developers', []),
                    'publishers': app_details.get('publishers', [])
                }
            
            return {'valid': False, 'error': 'App not found or invalid App ID'}
            
        except Exception as e:
            return {'valid': False, 'error': str(e)}
    
    def get_performance_summary(self, customer_id: str, days: int = 7) -> Dict[str, Any]:
        try:
            with db.get_connection() as conn:
                cursor = conn.cursor()
                
                # Get latest Steam data
                cursor.execute("""
                    SELECT 
                        app_name,
                        wishlist_count,
                        followers_count,
                        review_score,
                        review_count,
                        collected_at
                    FROM steam_data 
                    WHERE customer_id = ? 
                    ORDER BY collected_at DESC 
                    LIMIT 2
                """, (customer_id,))
                
                results = cursor.fetchall()
                
                if not results:
                    return {}
                
                latest = dict(results[0])
                previous = dict(results[1]) if len(results) > 1 else latest
                
                # Calculate changes
                wishlist_change = latest['wishlist_count'] - previous['wishlist_count']
                followers_change = latest['followers_count'] - previous['followers_count']
                review_change = latest['review_count'] - previous['review_count']
                
                summary = {
                    'app_name': latest['app_name'],
                    'current_metrics': {
                        'wishlist_count': latest['wishlist_count'],
                        'followers_count': latest['followers_count'],
                        'review_score': latest['review_score'],
                        'review_count': latest['review_count']
                    },
                    'changes': {
                        'wishlist_change': wishlist_change,
                        'followers_change': followers_change,
                        'review_change': review_change
                    },
                    'last_updated': latest['collected_at']
                }
                
                return summary
                
        except Exception as e:
            self.logger.error(f"Error getting performance summary for {customer_id}: {e}")
            return {}
    
    def search_steam_app(self, search_term: str) -> List[Dict[str, Any]]:
        try:
            # Steam doesn't have a public search API, so we'll use SteamSpy
            url = "https://steamspy.com/api.php"
            params = {
                'request': 'all',
                'page': '0'
            }
            
            response = self.session.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                # Filter results by search term
                matches = []
                for app_id, app_data in data.items():
                    if isinstance(app_data, dict) and 'name' in app_data:
                        if search_term.lower() in app_data['name'].lower():
                            matches.append({
                                'appid': int(app_id),
                                'name': app_data['name'],
                                'developer': app_data.get('developer', ''),
                                'publisher': app_data.get('publisher', ''),
                                'owners': app_data.get('owners', '0 .. 0')
                            })
                            
                            # Limit results
                            if len(matches) >= 10:
                                break
                
                return matches
            
            return []
            
        except Exception as e:
            self.logger.error(f"Error searching for Steam app {search_term}: {e}")
            return []
    
    def get_utm_campaign_data(self, customer_id: str) -> Dict[str, Any]:
        # Placeholder for UTM campaign tracking
        # This would require Steam Partner API access or custom tracking
        try:
            self.logger.info(f"UTM campaign tracking not yet implemented for {customer_id}")
            return {
                'campaigns': [],
                'total_clicks': 0,
                'conversions': 0,
                'note': 'UTM tracking requires Steam Partner API access'
            }
        except Exception as e:
            self.logger.error(f"Error getting UTM data for {customer_id}: {e}")
            return {}

# Global instance
steam_collector = SteamCollector()