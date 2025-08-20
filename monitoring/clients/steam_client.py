#!/usr/bin/env python3
"""
Client for interacting with the Steamworks Web API.
"""

import os
import requests

class SteamClient:
    BASE_URL = "https://partner.steam-api.com"

    def __init__(self):
        """
        Initializes the Steam client with credentials from environment variables.
        """
        self.api_key = os.getenv('STEAM_API_KEY')
        self.app_id = os.getenv('STEAM_APPID')

        if not self.api_key or not self.app_id:
            raise ValueError("STEAM_API_KEY or STEAM_APPID not found in environment variables.")

        print("Steam client initialized.")

    def get_wishlist_data(self):
        """
        Fetches the current wishlist count for the configured App ID.
        Note: The Steamworks API for wishlist data is not publicly documented in detail.
        This implementation is based on common patterns for the partner API.
        The endpoint and response structure might need adjustment.

        Returns:
            A dictionary with wishlist data or None if an error occurs.
        """
        endpoint = f"{self.BASE_URL}/IPublisherApp/GetWishlistData/v1/"
        params = {
            'key': self.api_key,
            'appid': self.app_id
        }

        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

            data = response.json()
            if data.get('response') and data['response'].get('success') == 1:
                # The exact structure of 'data' is not guaranteed.
                # We are assuming it contains a 'wishlist_count' field.
                wishlist_data = data['response'].get('data', {})
                return {
                    'wishlist_total': wishlist_data.get('wishlist_count', 0)
                }
            else:
                print(f"❌ Steam API returned an unsuccessful response: {data}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"❌ HTTP Request Error fetching Steam wishlist data: {e}")
            return None
        except ValueError:
            print(f"❌ Error decoding JSON from Steam API response.")
            return None
