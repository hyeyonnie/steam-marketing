from typing import Dict, Any
from .settings import settings

class APIConfig:
    def __init__(self):
        self.settings = settings
        
    def get_twitter_config(self) -> Dict[str, str]:
        return {
            "api_key": self.settings.twitter_api_key,
            "api_secret": self.settings.twitter_api_secret,
            "access_token": self.settings.twitter_access_token,
            "access_token_secret": self.settings.twitter_access_token_secret
        }
    
    def get_youtube_config(self) -> Dict[str, str]:
        return {
            "api_key": self.settings.youtube_api_key,
            "client_id": self.settings.google_client_id,
            "client_secret": self.settings.google_client_secret
        }
    
    def get_steam_config(self) -> Dict[str, str]:
        return {
            "api_key": self.settings.steam_api_key
        }
    
    def get_notion_config(self) -> Dict[str, str]:
        return {
            "api_key": self.settings.notion_api_key,
            "database_id": self.settings.notion_database_id
        }
    
    def get_rate_limit(self, service: str) -> int:
        rate_limits = self.settings.get_rate_limits()
        return rate_limits.get(service, 60)
    
    def get_endpoints(self) -> Dict[str, Dict[str, str]]:
        return {
            "twitter": {
                "base_url": "https://api.twitter.com/2",
                "user_lookup": "/users/by/username/{username}",
                "user_tweets": "/users/{user_id}/tweets",
                "tweet_metrics": "/tweets/{tweet_id}"
            },
            "youtube": {
                "base_url": "https://www.googleapis.com/youtube/v3",
                "channels": "/channels",
                "videos": "/videos",
                "search": "/search",
                "analytics": "/analytics"
            },
            "steam": {
                "base_url": "https://api.steampowered.com",
                "partner_base": "https://partner.steam-api.com",
                "app_details": "/appdetails",
                "user_stats": "/ISteamUserStats/GetUserStatsForGame/v0002/"
            },
            "notion": {
                "base_url": "https://api.notion.com/v1",
                "databases": "/databases",
                "pages": "/pages",
                "blocks": "/blocks"
            }
        }

api_config = APIConfig()