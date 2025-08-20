#!/usr/bin/env python3
"""
Client for interacting with the Twitter API using Tweepy.
"""

import os
import tweepy
from datetime import datetime, timezone

class TwitterClient:
    def __init__(self):
        """
        Initializes the Tweepy client with credentials from environment variables.
        Assumes OAuth 1.0a user context credentials are provided.
        """
        consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
        consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
        access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

        if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
            raise ValueError("Twitter API credentials not found in environment variables.")

        try:
            self.client = tweepy.Client(
                consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                access_token=access_token,
                access_token_secret=access_token_secret
            )
            print("Twitter client initialized.")
        except Exception as e:
            print(f"❌ Error initializing Twitter client: {e}")
            self.client = None

    def get_me(self):
        """
        Fetches the authenticated user's details, including follower count.
        
        Returns:
            A Tweepy User object or None if an error occurs.
        """
        if not self.client:
            return None
        try:
            # The 'user.fields' parameter is used to request additional fields.
            response = self.client.get_me(user_fields=["public_metrics"])
            return response.data
        except Exception as e:
            print(f"❌ Error fetching authenticated user from Twitter: {e}")
            return None

    def get_daily_tweets(self, user_id):
        """
        Fetches tweets posted by a specific user for the current day (UTC).

        Args:
            user_id (str): The ID of the Twitter user.

        Returns:
            A list of Tweepy Tweet objects or an empty list if an error occurs.
        """
        if not self.client or not user_id:
            return []
        
        # Get the start of the current day in UTC
        today = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
        
        try:
            response = self.client.get_users_tweets(
                id=user_id,
                start_time=today,
                tweet_fields=["public_metrics", "created_at"]
            )
            return response.data or []
        except Exception as e:
            print(f"❌ Error fetching daily tweets for user {user_id}: {e}")
            return []
