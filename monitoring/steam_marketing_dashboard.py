#!/usr/bin/env python3
"""
Steam Marketing Dashboard Backend
This script automates the process of fetching data from various platforms
(Twitter, YouTube, Steam) and updating a Notion dashboard.
"""

import os
import time
import schedule
from dotenv import load_dotenv
from datetime import datetime

# --- API Client Imports ---
from clients.twitter_client import TwitterClient
from clients.youtube_client import YouTubeClient
from clients.steam_client import SteamClient
from clients.notion_client import NotionClient

class MarketingDashboard:
    def __init__(self):
        """
        Initializes the dashboard, loads environment variables,
        and sets up API clients.
        """
        print("Initializing Marketing Dashboard...")
        load_dotenv(dotenv_path='../.env') # Load .env from the root directory

        # Load Notion Database IDs
        self.steam_db_id = os.getenv('STEAM_WISHLIST_DB_ID')
        self.twitter_db_id = os.getenv('TWITTER_DB_ID')
        self.youtube_db_id = os.getenv('YOUTUBE_DB_ID')
        self.influencer_db_id = os.getenv('INFLUENCER_DB_ID')
        self.press_db_id = os.getenv('PRESS_DB_ID')
        self.events_db_id = os.getenv('EVENTS_DB_ID')

        # --- Initialize API Clients ---
        try:
            self.twitter_client = TwitterClient()
        except ValueError as e:
            print(f"⚠️  {e}")
            self.twitter_client = None

        try:
            self.youtube_client = YouTubeClient()
        except ValueError as e:
            print(f"⚠️  {e}")
            self.youtube_client = None

        try:
            self.steam_client = SteamClient()
        except ValueError as e:
            print(f"⚠️  {e}")
            self.steam_client = None

        self.notion_client = NotionClient()
        print("Dashboard initialized successfully.")

    def fetch_twitter_data(self):
        """
        Fetches daily Twitter performance data using the TwitterClient.
        """
        print("Fetching Twitter data...")
        if not self.twitter_client:
            print("⚠️  Twitter client not initialized. Skipping.")
            return None

        user_info = self.twitter_client.get_me()
        if not user_info or not user_info.public_metrics:
            print("Could not fetch user info from Twitter.")
            return None

        followers_count = user_info.public_metrics.get('followers_count', 0)
        user_id = user_info.id
        daily_tweets_raw = self.twitter_client.get_daily_tweets(user_id)
        processed_tweets = []
        for tweet in daily_tweets_raw:
            metrics = tweet.public_metrics or {}
            processed_tweets.append({
                'text': tweet.text,
                'likes': metrics.get('like_count', 0),
                'retweets': metrics.get('retweet_count', 0),
                'replies': metrics.get('reply_count', 0),
                'impressions': metrics.get('impression_count', 0)
            })
        twitter_data = {
            'followers': followers_count,
            'daily_tweets': processed_tweets
        }
        print(f"✅ Twitter data fetched for user: {user_info.username}.")
        return twitter_data

    def fetch_youtube_data(self):
        """
        Fetches daily YouTube performance data using the YouTubeClient.
        """
        print("Fetching YouTube data...")
        if not self.youtube_client or not self.youtube_client.youtube:
            print("⚠️  YouTube client not initialized. Skipping.")
            return None

        channel_stats = self.youtube_client.get_channel_stats()
        if not channel_stats:
            print("Could not fetch channel stats from YouTube.")
            return None

        sub_count = int(channel_stats['statistics'].get('subscriberCount', 0))
        channel_id = channel_stats['id']
        channel_name = channel_stats['snippet']['title']
        daily_videos_raw = self.youtube_client.get_daily_videos(channel_id)
        processed_videos = []
        for video in daily_videos_raw:
            stats = video.get('statistics', {})
            processed_videos.append({
                'id': video['id'],
                'title': video['snippet']['title'],
                'views': int(stats.get('viewCount', 0)),
                'likes': int(stats.get('likeCount', 0)),
                'comments': int(stats.get('commentCount', 0))
            })
        youtube_data = {
            'subscribers': sub_count,
            'daily_videos': processed_videos
        }
        print(f"✅ YouTube data fetched for channel: {channel_name}.")
        return youtube_data

    def fetch_steam_data(self):
        """
        Fetches daily Steam performance data using the SteamClient.
        """
        print("Fetching Steam data...")
        if not self.steam_client:
            print("⚠️  Steam client not initialized. Skipping.")
            return None

        wishlist_data = self.steam_client.get_wishlist_data()
        if not wishlist_data:
            print("Could not fetch wishlist data from Steam.")
            return None

        # Note: Calculating daily/weekly change requires storing historical data,
        # which is a feature to be added later.
        steam_data = {
            'wishlists': wishlist_data.get('wishlist_total', 0),
            'daily_change': 0  # Placeholder
        }
        print(f"✅ Steam data fetched.")
        return steam_data

    def update_notion_dashboard(self, twitter_data, youtube_data, steam_data):
        """
        Updates the Notion databases with the latest fetched data.
        """
        print("Updating Notion dashboard...")
        today_str = datetime.now().strftime("%Y-%m-%d")

        # --- Update Twitter Database ---
        if self.twitter_db_id and twitter_data:
            daily_tweets = twitter_data.get('daily_tweets', [])
            twitter_properties = {
                'Date': {'date': {'start': today_str}},
                'Followers': {'number': twitter_data.get('followers')},
                'Posts Count': {'number': len(daily_tweets)},
                'Likes': {'number': sum(t['likes'] for t in daily_tweets)},
                'Retweets': {'number': sum(t['retweets'] for t in daily_tweets)},
                'Comments': {'number': sum(t['replies'] for t in daily_tweets)},
                'Impressions': {'number': sum(t['impressions'] for t in daily_tweets)}
            }
            self.notion_client.add_row_to_database(self.twitter_db_id, twitter_properties)

        # --- Update YouTube Database ---
        if self.youtube_db_id and youtube_data:
            subscribers_count = youtube_data.get('subscribers')
            for video in youtube_data.get('daily_videos', []):
                video_properties = {
                    'Date': {'date': {'start': today_str}},
                    'Subscribers': {'number': subscribers_count},
                    'Video Title': {'title': [{'text': {'content': video['title']}}],
                    'Video URL': {'url': f"https://www.youtube.com/watch?v={video['id']}"},
                    'Views': {'number': video['views']},
                    'Likes': {'number': video['likes']},
                    'Comments': {'number': video['comments']}
                }
                self.notion_client.add_row_to_database(self.youtube_db_id, video_properties)

        # --- Update Steam Database ---
        if self.steam_db_id and steam_data:
            steam_properties = {
                'Date': {'date': {'start': today_str}},
                'Wishlist Count': {'number': steam_data.get('wishlists')},
                'Daily Change': {'number': steam_data.get('daily_change')} # Will be 0 for now
            }
            self.notion_client.add_row_to_database(self.steam_db_id, steam_properties)

        print("✅ Notion dashboard updated.")

    def daily_update_job(self):
        """
        The main job that runs daily, orchestrating the fetching and updating process.
        """
        print("\n" + "="*50)
        print(f"🚀 Starting daily update job at {time.ctime()}")
        print("="*50)
        
        try:
            twitter_data = self.fetch_twitter_data()
            youtube_data = self.fetch_youtube_data()
            steam_data = self.fetch_steam_data()

            self.update_notion_dashboard(
                twitter_data,
                youtube_data,
                steam_data
            )
            
            print("\n" + "="*50)
            print(f"✅ Daily update job finished successfully at {time.ctime()}")
            print("="*50)

        except Exception as e:
            print(f"❌ An error occurred during the daily update: {e}")

def main():
    """
    Main function to start the scheduler.
    """
    dashboard = MarketingDashboard()

    # For production, you might want to run this once and have a system service (like systemd)
    # or a cron job manage the execution, rather than a long-running Python script.
    print("Scheduler started. Waiting for the scheduled job to run...")
    schedule.every().day.at("01:00").do(dashboard.daily_update_job)
    
    # For testing, you can uncomment the following lines:
    # print("Running one-time job immediately for testing purposes.")
    # dashboard.daily_update_job()
    # schedule.every(1).minutes.do(dashboard.daily_update_job) 

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()