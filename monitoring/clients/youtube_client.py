#!/usr/bin/env python3
"""
Client for interacting with the YouTube Data API.
"""

import os
import json
from datetime import datetime, timezone

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class YouTubeClient:
    def __init__(self, client_secrets_path='../client_secrets.json'):
        """
        Initializes the YouTube Data API client.
        Handles OAuth 2.0 authentication using a refresh token.
        """
        self.youtube = None
        refresh_token = os.getenv('YOUTUBE_REFRESH_TOKEN')

        if not os.path.exists(client_secrets_path):
            print(f"❌ Error: Client secrets file not found at {client_secrets_path}")
            return
            
        if not refresh_token:
            print("❌ Error: YOUTUBE_REFRESH_TOKEN not found in environment variables.")
            return

        try:
            with open(client_secrets_path, 'r') as f:
                client_config = json.load(f)['web']

            creds = Credentials.from_authorized_user_info(
                info={'refresh_token': refresh_token,
                      'client_id': client_config['client_id'],
                      'client_secret': client_config['client_secret']},
                scopes=['https://www.googleapis.com/auth/youtube.readonly']
            )

            # Refresh the token if it's expired
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())

            self.youtube = build('youtube', 'v3', credentials=creds)
            print("YouTube client initialized.")

        except Exception as e:
            print(f"❌ Error initializing YouTube client: {e}")

    def get_channel_stats(self):
        """
        Fetches statistics for the authenticated user's channel.
        """
        if not self.youtube:
            return None
        try:
            response = self.youtube.channels().list(
                part='snippet,statistics',
                mine=True
            ).execute()
            
            if 'items' in response and len(response['items']) > 0:
                return response['items'][0]
            return None
        except HttpError as e:
            print(f"❌ YouTube API Error fetching channel stats: {e}")
            return None

    def get_daily_videos(self, channel_id):
        """
        Fetches videos uploaded today for a specific channel.
        """
        if not self.youtube or not channel_id:
            return []

        today_start = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
        
        try:
            # First, search for videos uploaded today
            search_response = self.youtube.search().list(
                part='id',
                channelId=channel_id,
                publishedAfter=today_start.isoformat(),
                type='video',
                maxResults=50 # Max allowed
            ).execute()

            video_ids = [item['id']['videoId'] for item in search_response.get('items', [])]

            if not video_ids:
                return []

            # Second, get the statistics for the found videos
            video_response = self.youtube.videos().list(
                part='snippet,statistics',
                id=','.join(video_ids)
            ).execute()

            return video_response.get('items', [])
        except HttpError as e:
            print(f"❌ YouTube API Error fetching daily videos: {e}")
            return []
