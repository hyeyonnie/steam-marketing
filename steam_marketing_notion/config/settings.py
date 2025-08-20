import os
import yaml
from pathlib import Path
from typing import Dict, Any
from dotenv import load_dotenv

class Settings:
    def __init__(self, config_file: str = "config.yaml"):
        load_dotenv()
        
        self.base_dir = Path(__file__).parent.parent
        self.config_file = self.base_dir / config_file
        self.config = self._load_config()
        
        # Environment variables
        self.twitter_api_key = os.getenv("TWITTER_API_KEY")
        self.twitter_api_secret = os.getenv("TWITTER_API_SECRET")
        self.twitter_access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        self.twitter_access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        
        self.youtube_api_key = os.getenv("YOUTUBE_API_KEY")
        self.google_client_id = os.getenv("GOOGLE_CLIENT_ID")
        self.google_client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
        
        self.steam_api_key = os.getenv("STEAM_API_KEY")
        
        self.notion_api_key = os.getenv("NOTION_API_KEY")
        self.notion_database_id = os.getenv("NOTION_DATABASE_ID")
        
        self.database_path = os.getenv("DATABASE_PATH", "./data/marketing_data.db")
        self.log_level = os.getenv("LOG_LEVEL", "INFO")
        self.log_file = os.getenv("LOG_FILE", "./logs/marketing_scheduler.log")
        
        # Email settings
        self.smtp_server = os.getenv("SMTP_SERVER")
        self.smtp_port = int(os.getenv("SMTP_PORT", 587))
        self.email_user = os.getenv("EMAIL_USER")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.alert_email = os.getenv("ALERT_EMAIL")
        
    def _load_config(self) -> Dict[str, Any]:
        try:
            with open(self.config_file, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f"Config file {self.config_file} not found. Using defaults.")
            return self._default_config()
        except yaml.YAMLError as e:
            print(f"Error parsing config file: {e}. Using defaults.")
            return self._default_config()
    
    def _default_config(self) -> Dict[str, Any]:
        return {
            "schedule": {
                "daily_collection_time": "02:00",
                "weekly_collection_day": "sunday",
                "weekly_collection_time": "03:00",
                "customer_config_check_interval": 300
            },
            "rate_limits": {
                "twitter": 75,
                "youtube": 10000,
                "steam": 100,
                "notion": 3
            },
            "retry": {
                "max_attempts": 3,
                "backoff_factor": 2,
                "max_delay": 300
            },
            "data_collection": {
                "twitter": {
                    "fetch_tweets_hours": 24,
                    "include_retweets": False,
                    "include_replies": False
                },
                "youtube": {
                    "fetch_videos_hours": 24,
                    "include_shorts": True
                },
                "steam": {
                    "track_wishlists": True,
                    "track_utm_campaigns": True
                }
            },
            "logging": {
                "level": "INFO",
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "max_file_size": 10485760,
                "backup_count": 5
            }
        }
    
    def get(self, key: str, default=None):
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def get_schedule_config(self) -> Dict[str, Any]:
        return self.config.get("schedule", {})
    
    def get_rate_limits(self) -> Dict[str, int]:
        return self.config.get("rate_limits", {})
    
    def get_retry_config(self) -> Dict[str, Any]:
        return self.config.get("retry", {})
    
    def get_data_collection_config(self) -> Dict[str, Any]:
        return self.config.get("data_collection", {})
    
    def get_logging_config(self) -> Dict[str, Any]:
        return self.config.get("logging", {})
    
    def validate_credentials(self) -> Dict[str, bool]:
        validation = {
            "twitter": all([
                self.twitter_api_key,
                self.twitter_api_secret,
                self.twitter_access_token,
                self.twitter_access_token_secret
            ]),
            "youtube": all([
                self.youtube_api_key,
                self.google_client_id,
                self.google_client_secret
            ]),
            "steam": bool(self.steam_api_key),
            "notion": all([
                self.notion_api_key,
                self.notion_database_id
            ])
        }
        
        return validation

settings = Settings()