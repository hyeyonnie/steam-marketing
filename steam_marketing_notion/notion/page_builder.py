import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
from .notion_client import notion_client

class PageBuilder:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def create_customer_dashboard(self, customer_id: str, parent_page_id: str) -> Optional[str]:
        try:
            # Create main dashboard page
            dashboard_properties = {
                "title": {
                    "title": [
                        {
                            "type": "text",
                            "text": {
                                "content": f"Marketing Dashboard - {customer_id}"
                            }
                        }
                    ]
                }
            }
            
            # Create dashboard content blocks
            dashboard_blocks = [
                notion_client.create_heading_block("📊 Marketing Dashboard", 1),
                notion_client.create_text_block(f"Customer: {customer_id}"),
                notion_client.create_text_block(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}"),
                
                notion_client.create_heading_block("🎯 Quick Metrics", 2),
                notion_client.create_callout_block("Daily metrics will appear here automatically", "⏱️"),
                
                notion_client.create_heading_block("📱 Social Media Performance", 2),
                notion_client.create_text_block("Detailed social media analytics and engagement metrics"),
                
                notion_client.create_heading_block("🎮 Steam Performance", 2),
                notion_client.create_text_block("Wishlist counts, reviews, and game performance data"),
                
                notion_client.create_heading_block("📰 Press & Mentions", 2),
                notion_client.create_text_block("Recent press coverage and social media mentions")
            ]
            
            dashboard_page_id = notion_client.create_page(
                parent_page_id, 
                dashboard_properties,
                dashboard_blocks
            )
            
            if dashboard_page_id:
                self.logger.info(f"Created dashboard page for customer {customer_id}")
                return dashboard_page_id
            
            return None
            
        except Exception as e:
            self.logger.error(f"Error creating customer dashboard: {e}")
            return None
    
    def create_setup_databases(self, parent_page_id: str) -> Dict[str, str]:
        try:
            database_ids = {}
            
            # Create Twitter connection database
            twitter_db_id = self._create_twitter_connection_db(parent_page_id)
            if twitter_db_id:
                database_ids['twitter'] = twitter_db_id
            
            # Create YouTube connection database
            youtube_db_id = self._create_youtube_connection_db(parent_page_id)
            if youtube_db_id:
                database_ids['youtube'] = youtube_db_id
            
            # Create Steam connection database
            steam_db_id = self._create_steam_connection_db(parent_page_id)
            if steam_db_id:
                database_ids['steam'] = steam_db_id
            
            self.logger.info(f"Created {len(database_ids)} setup databases")
            return database_ids
            
        except Exception as e:
            self.logger.error(f"Error creating setup databases: {e}")
            return {}
    
    def _create_twitter_connection_db(self, parent_page_id: str) -> Optional[str]:
        properties = {
            "Name": {
                "title": {}
            },
            "API Key": {
                "rich_text": {}
            },
            "API Secret": {
                "rich_text": {}
            },
            "Access Token": {
                "rich_text": {}
            },
            "Access Token Secret": {
                "rich_text": {}
            },
            "Username": {
                "rich_text": {}
            },
            "Connection Status": {
                "select": {
                    "options": [
                        {"name": "Pending", "color": "yellow"},
                        {"name": "Connected", "color": "green"},
                        {"name": "Failed", "color": "red"},
                        {"name": "Testing", "color": "blue"}
                    ]
                }
            },
            "Last Sync": {
                "date": {}
            },
            "Setup Date": {
                "created_time": {}
            }
        }
        
        return notion_client.create_database(parent_page_id, "Twitter/X Connection", properties)
    
    def _create_youtube_connection_db(self, parent_page_id: str) -> Optional[str]:
        properties = {
            "Name": {
                "title": {}
            },
            "Channel ID": {
                "rich_text": {}
            },
            "Channel Name": {
                "rich_text": {}
            },
            "API Key": {
                "rich_text": {}
            },
            "Connection Status": {
                "select": {
                    "options": [
                        {"name": "Pending", "color": "yellow"},
                        {"name": "Connected", "color": "green"},
                        {"name": "Failed", "color": "red"},
                        {"name": "Testing", "color": "blue"}
                    ]
                }
            },
            "Subscriber Count": {
                "number": {}
            },
            "Last Sync": {
                "date": {}
            },
            "Setup Date": {
                "created_time": {}
            }
        }
        
        return notion_client.create_database(parent_page_id, "YouTube Connection", properties)
    
    def _create_steam_connection_db(self, parent_page_id: str) -> Optional[str]:
        properties = {
            "Name": {
                "title": {}
            },
            "App ID": {
                "number": {}
            },
            "App Name": {
                "rich_text": {}
            },
            "API Key": {
                "rich_text": {}
            },
            "Connection Status": {
                "select": {
                    "options": [
                        {"name": "Pending", "color": "yellow"},
                        {"name": "Connected", "color": "green"},
                        {"name": "Failed", "color": "red"},
                        {"name": "Testing", "color": "blue"}
                    ]
                }
            },
            "Wishlist Count": {
                "number": {}
            },
            "Last Sync": {
                "date": {}
            },
            "Setup Date": {
                "created_time": {}
            }
        }
        
        return notion_client.create_database(parent_page_id, "Steam Connection", properties)
    
    def create_performance_databases(self, parent_page_id: str) -> Dict[str, str]:
        try:
            database_ids = {}
            
            # Create daily performance database
            daily_db_id = self._create_daily_performance_db(parent_page_id)
            if daily_db_id:
                database_ids['daily_performance'] = daily_db_id
            
            # Create content database
            content_db_id = self._create_content_db(parent_page_id)
            if content_db_id:
                database_ids['content'] = content_db_id
            
            # Create events & press database
            events_db_id = self._create_events_press_db(parent_page_id)
            if events_db_id:
                database_ids['events_press'] = events_db_id
            
            self.logger.info(f"Created {len(database_ids)} performance databases")
            return database_ids
            
        except Exception as e:
            self.logger.error(f"Error creating performance databases: {e}")
            return {}
    
    def _create_daily_performance_db(self, parent_page_id: str) -> Optional[str]:
        properties = {
            "Date": {
                "title": {}
            },
            "Platform": {
                "select": {
                    "options": [
                        {"name": "Twitter", "color": "blue"},
                        {"name": "YouTube", "color": "red"},
                        {"name": "Steam", "color": "purple"},
                        {"name": "Overall", "color": "gray"}
                    ]
                }
            },
            "Followers/Subscribers": {
                "number": {}
            },
            "Daily Change": {
                "number": {}
            },
            "Engagement Rate": {
                "number": {}
            },
            "Content Count": {
                "number": {}
            },
            "Top Performing Content": {
                "rich_text": {}
            },
            "Notes": {
                "rich_text": {}
            },
            "Created": {
                "created_time": {}
            }
        }
        
        return notion_client.create_database(parent_page_id, "Daily Performance", properties)
    
    def _create_content_db(self, parent_page_id: str) -> Optional[str]:
        properties = {
            "Title": {
                "title": {}
            },
            "Platform": {
                "select": {
                    "options": [
                        {"name": "Twitter", "color": "blue"},
                        {"name": "YouTube", "color": "red"},
                        {"name": "TikTok", "color": "pink"},
                        {"name": "Instagram", "color": "orange"}
                    ]
                }
            },
            "Content Type": {
                "select": {
                    "options": [
                        {"name": "Post", "color": "blue"},
                        {"name": "Video", "color": "red"},
                        {"name": "Story", "color": "yellow"},
                        {"name": "Reel", "color": "purple"}
                    ]
                }
            },
            "Published Date": {
                "date": {}
            },
            "Views/Impressions": {
                "number": {}
            },
            "Likes": {
                "number": {}
            },
            "Comments": {
                "number": {}
            },
            "Shares/Retweets": {
                "number": {}
            },
            "Engagement Rate": {
                "number": {}
            },
            "Link": {
                "url": {}
            },
            "Performance": {
                "select": {
                    "options": [
                        {"name": "Excellent", "color": "green"},
                        {"name": "Good", "color": "blue"},
                        {"name": "Average", "color": "yellow"},
                        {"name": "Poor", "color": "red"}
                    ]
                }
            },
            "Created": {
                "created_time": {}
            }
        }
        
        return notion_client.create_database(parent_page_id, "Content Database", properties)
    
    def _create_events_press_db(self, parent_page_id: str) -> Optional[str]:
        properties = {
            "Title": {
                "title": {}
            },
            "Type": {
                "select": {
                    "options": [
                        {"name": "Press", "color": "blue"},
                        {"name": "Event", "color": "green"},
                        {"name": "Mention", "color": "yellow"},
                        {"name": "Review", "color": "purple"},
                        {"name": "Interview", "color": "orange"}
                    ]
                }
            },
            "Source": {
                "rich_text": {}
            },
            "URL": {
                "url": {}
            },
            "Status": {
                "select": {
                    "options": [
                        {"name": "Detected", "color": "yellow"},
                        {"name": "Reviewed", "color": "blue"},
                        {"name": "Responded", "color": "green"},
                        {"name": "Archived", "color": "gray"}
                    ]
                }
            },
            "Event Date": {
                "date": {}
            },
            "Description": {
                "rich_text": {}
            },
            "Impact": {
                "select": {
                    "options": [
                        {"name": "High", "color": "red"},
                        {"name": "Medium", "color": "yellow"},
                        {"name": "Low", "color": "gray"}
                    ]
                }
            },
            "Created": {
                "created_time": {}
            }
        }
        
        return notion_client.create_database(parent_page_id, "Events & Press", properties)
    
    def update_dashboard_summary(self, dashboard_page_id: str, summary_data: Dict[str, Any]) -> bool:
        try:
            # Create summary blocks
            summary_blocks = [
                notion_client.create_heading_block("📊 Today's Summary", 2),
                notion_client.create_text_block(f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}"),
            ]
            
            # Add platform metrics
            for platform, metrics in summary_data.get('platforms', {}).items():
                platform_emoji = {"twitter": "🐦", "youtube": "📺", "steam": "🎮"}.get(platform, "📱")
                
                summary_blocks.append(
                    notion_client.create_heading_block(f"{platform_emoji} {platform.title()}", 3)
                )
                
                if platform == 'twitter':
                    followers = metrics.get('followers_count', 0)
                    engagement = metrics.get('total_engagement', 0)
                    summary_blocks.append(
                        notion_client.create_callout_block(
                            f"Followers: {followers:,}\nTotal Engagement: {engagement:,}",
                            "🐦"
                        )
                    )
                elif platform == 'youtube':
                    subscribers = metrics.get('subscriber_count', 0)
                    views = metrics.get('total_views', 0)
                    summary_blocks.append(
                        notion_client.create_callout_block(
                            f"Subscribers: {subscribers:,}\nTotal Views: {views:,}",
                            "📺"
                        )
                    )
                elif platform == 'steam':
                    wishlist = metrics.get('wishlist_count', 0)
                    followers = metrics.get('followers_count', 0)
                    summary_blocks.append(
                        notion_client.create_callout_block(
                            f"Wishlist: {wishlist:,}\nFollowers: {followers:,}",
                            "🎮"
                        )
                    )
            
            # Append blocks to dashboard page
            success = notion_client.append_blocks(dashboard_page_id, summary_blocks)
            
            if success:
                self.logger.info(f"Updated dashboard summary for page {dashboard_page_id}")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Error updating dashboard summary: {e}")
            return False

# Global instance
page_builder = PageBuilder()