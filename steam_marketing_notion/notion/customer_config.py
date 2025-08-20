import logging
import json
from datetime import datetime
from typing import Dict, List, Any, Optional
from .notion_client import notion_client
from database import db
from collectors import twitter_collector, youtube_collector, steam_collector

class CustomerConfigMonitor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.setup_databases = {}
    
    def check_for_updates(self) -> Dict[str, Any]:
        try:
            updates = {}
            customers = db.get_all_customers()
            
            for customer in customers:
                customer_id = customer['customer_id']
                notion_page_id = customer['notion_page_id']
                
                # Check each platform's connection database
                customer_updates = self._check_customer_updates(customer_id, notion_page_id)
                
                if customer_updates:
                    updates[customer_id] = customer_updates
            
            return updates
            
        except Exception as e:
            self.logger.error(f"Error checking for configuration updates: {e}")
            return {}
    
    def _check_customer_updates(self, customer_id: str, notion_page_id: str) -> Dict[str, Any]:
        try:
            updates = {}
            
            # Find setup databases for this customer
            setup_databases = self._find_setup_databases(notion_page_id)
            
            for platform, database_id in setup_databases.items():
                if database_id:
                    platform_updates = self._check_platform_updates(customer_id, platform, database_id)
                    if platform_updates:
                        updates[platform] = platform_updates
            
            return updates
            
        except Exception as e:
            self.logger.error(f"Error checking updates for customer {customer_id}: {e}")
            return {}
    
    def _find_setup_databases(self, notion_page_id: str) -> Dict[str, str]:
        try:
            # Search for setup databases within the customer's page
            search_results = notion_client.search_pages(
                filter_conditions={
                    "property": "object",
                    "value": "database"
                }
            )
            
            databases = {}
            setup_keywords = {
                'twitter': ['twitter', 'x connection'],
                'youtube': ['youtube connection'],
                'steam': ['steam connection']
            }
            
            for result in search_results:
                title = result.get('title', [{}])[0].get('text', {}).get('content', '').lower()
                
                for platform, keywords in setup_keywords.items():
                    if any(keyword in title for keyword in keywords):
                        databases[platform] = result['id']
                        break
            
            return databases
            
        except Exception as e:
            self.logger.error(f"Error finding setup databases: {e}")
            return {}
    
    def _check_platform_updates(self, customer_id: str, platform: str, database_id: str) -> List[Dict[str, Any]]:
        try:
            # Query database for new or updated entries
            filter_conditions = {
                "or": [
                    {
                        "property": "Connection Status",
                        "select": {
                            "equals": "Pending"
                        }
                    },
                    {
                        "property": "Connection Status",
                        "select": {
                            "equals": "Testing"
                        }
                    }
                ]
            }
            
            results = notion_client.query_database(database_id, filter_conditions)
            
            updates = []
            for result in results:
                update_data = self._extract_connection_data(platform, result)
                if update_data:
                    updates.append(update_data)
            
            return updates
            
        except Exception as e:
            self.logger.error(f"Error checking {platform} updates: {e}")
            return []
    
    def _extract_connection_data(self, platform: str, notion_page: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        try:
            properties = notion_page.get('properties', {})
            
            if platform == 'twitter':
                return {
                    'page_id': notion_page['id'],
                    'platform': platform,
                    'api_key': self._get_property_value(properties, 'API Key'),
                    'api_secret': self._get_property_value(properties, 'API Secret'),
                    'access_token': self._get_property_value(properties, 'Access Token'),
                    'access_token_secret': self._get_property_value(properties, 'Access Token Secret'),
                    'username': self._get_property_value(properties, 'Username'),
                    'status': self._get_property_value(properties, 'Connection Status')
                }
            
            elif platform == 'youtube':
                return {
                    'page_id': notion_page['id'],
                    'platform': platform,
                    'channel_id': self._get_property_value(properties, 'Channel ID'),
                    'api_key': self._get_property_value(properties, 'API Key'),
                    'channel_name': self._get_property_value(properties, 'Channel Name'),
                    'status': self._get_property_value(properties, 'Connection Status')
                }
            
            elif platform == 'steam':
                return {
                    'page_id': notion_page['id'],
                    'platform': platform,
                    'app_id': self._get_property_value(properties, 'App ID'),
                    'api_key': self._get_property_value(properties, 'API Key'),
                    'app_name': self._get_property_value(properties, 'App Name'),
                    'status': self._get_property_value(properties, 'Connection Status')
                }
            
            return None
            
        except Exception as e:
            self.logger.error(f"Error extracting {platform} connection data: {e}")
            return None
    
    def _get_property_value(self, properties: Dict[str, Any], property_name: str) -> str:
        try:
            prop = properties.get(property_name, {})
            
            if prop.get('type') == 'rich_text':
                rich_text = prop.get('rich_text', [])
                if rich_text:
                    return rich_text[0].get('text', {}).get('content', '')
            
            elif prop.get('type') == 'title':
                title = prop.get('title', [])
                if title:
                    return title[0].get('text', {}).get('content', '')
            
            elif prop.get('type') == 'select':
                select = prop.get('select', {})
                if select:
                    return select.get('name', '')
            
            elif prop.get('type') == 'number':
                return str(prop.get('number', ''))
            
            return ''
            
        except:
            return ''
    
    def process_config_update(self, customer_id: str, config_data: Dict[str, Any]) -> bool:
        try:
            for platform, platform_data in config_data.items():
                if not isinstance(platform_data, list):
                    platform_data = [platform_data]
                
                for config in platform_data:
                    success = self._process_single_config(customer_id, platform, config)
                    
                    if success:
                        self.logger.info(f"Successfully processed {platform} config for {customer_id}")
                    else:
                        self.logger.warning(f"Failed to process {platform} config for {customer_id}")
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error processing config update for {customer_id}: {e}")
            return False
    
    def _process_single_config(self, customer_id: str, platform: str, config: Dict[str, Any]) -> bool:
        try:
            page_id = config.get('page_id')
            status = config.get('status', '').lower()
            
            if status == 'pending':
                # Validate the connection
                validation_result = self._validate_connection(platform, config)
                
                if validation_result.get('valid'):
                    # Update status to Connected
                    self._update_connection_status(page_id, 'Connected', validation_result)
                    
                    # Store connection data in database
                    connection_data = json.dumps(config)
                    db.update_social_connection(customer_id, platform, connection_data, 'connected')
                    
                    return True
                else:
                    # Update status to Failed
                    error_message = validation_result.get('error', 'Validation failed')
                    self._update_connection_status(page_id, 'Failed', {'error': error_message})
                    
                    return False
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error processing single {platform} config: {e}")
            return False
    
    def _validate_connection(self, platform: str, config: Dict[str, Any]) -> Dict[str, Any]:
        try:
            if platform == 'twitter':
                return twitter_collector.validate_connection_data(config)
            elif platform == 'youtube':
                return youtube_collector.validate_connection_data(config)
            elif platform == 'steam':
                return steam_collector.validate_connection_data(config)
            
            return {'valid': False, 'error': f'Unknown platform: {platform}'}
            
        except Exception as e:
            self.logger.error(f"Error validating {platform} connection: {e}")
            return {'valid': False, 'error': str(e)}
    
    def _update_connection_status(self, page_id: str, status: str, additional_data: Dict[str, Any] = None) -> bool:
        try:
            properties = {
                "Connection Status": {
                    "select": {
                        "name": status
                    }
                },
                "Last Sync": {
                    "date": {
                        "start": datetime.now().isoformat()
                    }
                }
            }
            
            # Add additional data if validation was successful
            if additional_data and status == 'Connected':
                if 'username' in additional_data:
                    properties["Username"] = {
                        "rich_text": [
                            {
                                "text": {
                                    "content": additional_data['username']
                                }
                            }
                        ]
                    }
                
                if 'channel_name' in additional_data:
                    properties["Channel Name"] = {
                        "rich_text": [
                            {
                                "text": {
                                    "content": additional_data['channel_name']
                                }
                            }
                        ]
                    }
                
                if 'app_name' in additional_data:
                    properties["App Name"] = {
                        "rich_text": [
                            {
                                "text": {
                                    "content": additional_data['app_name']
                                }
                            }
                        ]
                    }
                
                if 'subscriber_count' in additional_data:
                    properties["Subscriber Count"] = {
                        "number": additional_data['subscriber_count']
                    }
                
                if 'wishlist_count' in additional_data:
                    properties["Wishlist Count"] = {
                        "number": additional_data['wishlist_count']
                    }
            
            success = notion_client.update_page(page_id, properties)
            
            if success:
                self.logger.info(f"Updated connection status to {status} for page {page_id}")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Error updating connection status: {e}")
            return False
    
    def create_customer_setup(self, customer_id: str, parent_page_id: str) -> bool:
        try:
            from .page_builder import page_builder
            
            # Create setup databases
            setup_databases = page_builder.create_setup_databases(parent_page_id)
            
            if setup_databases:
                # Create dashboard
                dashboard_id = page_builder.create_customer_dashboard(customer_id, parent_page_id)
                
                if dashboard_id:
                    # Create performance databases
                    performance_databases = page_builder.create_performance_databases(dashboard_id)
                    
                    # Add customer to database
                    db.add_customer(customer_id, parent_page_id)
                    
                    self.logger.info(f"Created complete setup for customer {customer_id}")
                    return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"Error creating customer setup for {customer_id}: {e}")
            return False

# Global instance
customer_config_monitor = CustomerConfigMonitor()