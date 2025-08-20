#!/usr/bin/env python3
"""
Notion Dashboard Creator
Automatically creates all required databases for Steam Game Marketing Dashboard
"""

import requests
import json
import os
from datetime import datetime

class NotionDashboardCreator:
    def __init__(self):
        self.notion_token = os.getenv('NOTION_TOKEN')
        self.parent_page_id = os.getenv('NOTION_PARENT_PAGE_ID')  # The page where databases will be created
        self.notion_version = '2022-06-28'

        self.headers = {
            'Authorization': f'Bearer {self.notion_token}',
            'Content-Type': 'application/json',
            'Notion-Version': self.notion_version
        }

    def create_database(self, title, properties, parent_id):
        """Create a new database in Notion"""
        url = 'https://api.notion.com/v1/databases'

        data = {
            'parent': {
                'type': 'page_id',
                'page_id': parent_id
            },
            'title': [
                {
                    'type': 'text',
                    'text': {
                        'content': title
                    }
                }
            ],
            'properties': properties
        }

        response = requests.post(url, headers=self.headers, json=data)

        if response.status_code == 200:
            result = response.json()
            print(f"✅ Created database: {title}")
            print(f"   Database ID: {result['id']}")
            return result['id']
        else:
            print(f"❌ Error creating {title}: {response.status_code}")
            print(response.text)
            return None

    def create_all_databases(self):
        """Create all required databases for the marketing dashboard"""
        databases = {}

        # Steam Wishlist Tracking Database
        steam_properties = {
            'Date': {'date': {}},
            'Wishlist Count': {'number': {'format': 'number'}},
            'Daily Change': {'number': {'format': 'number'}},
            'Weekly Change': {'number': {'format': 'number'}},
            'Notes': {'rich_text': {}}
        }

        databases['steam'] = self.create_database(
            'Steam Wishlist Tracking', 
            steam_properties, 
            self.parent_page_id
        )

        # Twitter Analytics Database
        twitter_properties = {
            'Date': {'date': {}},
            'Followers': {'number': {'format': 'number'}},
            'Posts Count': {'number': {'format': 'number'}},
            'Likes': {'number': {'format': 'number'}},
            'Retweets': {'number': {'format': 'number'}},
            'Comments': {'number': {'format': 'number'}},
            'Impressions': {'number': {'format': 'number'}},
            'Post URL': {'url': {}},
            'Post Content': {'rich_text': {}}
        }

        databases['twitter'] = self.create_database(
            'Twitter Analytics', 
            twitter_properties, 
            self.parent_page_id
        )

        # YouTube Analytics Database
        youtube_properties = {
            'Date': {'date': {}},
            'Subscribers': {'number': {'format': 'number'}},
            'Video Title': {'title': {}},
            'Video URL': {'url': {}},
            'Views': {'number': {'format': 'number'}},
            'Likes': {'number': {'format': 'number'}},
            'Comments': {'number': {'format': 'number'}},
            'Watch Time (minutes)': {'number': {'format': 'number'}},
            'Type': {
                'select': {
                    'options': [
                        {'name': 'Video', 'color': 'blue'},
                        {'name': 'Short', 'color': 'red'}
                    ]
                }
            }
        }

        databases['youtube'] = self.create_database(
            'YouTube Analytics', 
            youtube_properties, 
            self.parent_page_id
        )

        # Influencer Coverage Database
        influencer_properties = {
            'Date': {'date': {}},
            'Influencer Name': {'title': {}},
            'Platform': {
                'select': {
                    'options': [
                        {'name': 'YouTube', 'color': 'red'},
                        {'name': 'Twitch', 'color': 'purple'},
                        {'name': 'TikTok', 'color': 'pink'},
                        {'name': 'Instagram', 'color': 'orange'},
                        {'name': 'Twitter', 'color': 'blue'}
                    ]
                }
            },
            'Content URL': {'url': {}},
            'Content Type': {
                'select': {
                    'options': [
                        {'name': 'Review', 'color': 'green'},
                        {'name': 'Gameplay', 'color': 'blue'},
                        {'name': 'Stream', 'color': 'purple'},
                        {'name': 'Mention', 'color': 'gray'},
                        {'name': 'Interview', 'color': 'yellow'}
                    ]
                }
            },
            'Reach (Views/Followers)': {'number': {'format': 'number'}},
            'Engagement': {'number': {'format': 'number'}},
            'Sentiment': {
                'select': {
                    'options': [
                        {'name': 'Positive', 'color': 'green'},
                        {'name': 'Neutral', 'color': 'yellow'},
                        {'name': 'Negative', 'color': 'red'}
                    ]
                }
            },
            'Notes': {'rich_text': {}}
        }

        databases['influencer'] = self.create_database(
            'Influencer Coverage', 
            influencer_properties, 
            self.parent_page_id
        )

        # Press & Articles Database
        press_properties = {
            'Date': {'date': {}},
            'Outlet': {'title': {}},
            'Article Title': {'rich_text': {}},
            'Article URL': {'url': {}},
            'Author': {'rich_text': {}},
            'Type': {
                'select': {
                    'options': [
                        {'name': 'Review', 'color': 'green'},
                        {'name': 'Preview', 'color': 'blue'},
                        {'name': 'Interview', 'color': 'yellow'},
                        {'name': 'News', 'color': 'red'},
                        {'name': 'Feature', 'color': 'purple'}
                    ]
                }
            },
            'Tier': {
                'select': {
                    'options': [
                        {'name': 'Tier 1', 'color': 'red'},
                        {'name': 'Tier 2', 'color': 'orange'},
                        {'name': 'Tier 3', 'color': 'yellow'},
                        {'name': 'Blog', 'color': 'gray'}
                    ]
                }
            },
            'Sentiment': {
                'select': {
                    'options': [
                        {'name': 'Positive', 'color': 'green'},
                        {'name': 'Neutral', 'color': 'yellow'},
                        {'name': 'Negative', 'color': 'red'}
                    ]
                }
            },
            'Summary': {'rich_text': {}}
        }

        databases['press'] = self.create_database(
            'Press & Articles', 
            press_properties, 
            self.parent_page_id
        )

        # Events & Applications Database
        events_properties = {
            'Event Name': {'title': {}},
            'Event Date': {'date': {}},
            'Application Deadline': {'date': {}},
            'Status': {
                'select': {
                    'options': [
                        {'name': 'Not Applied', 'color': 'gray'},
                        {'name': 'Applied', 'color': 'yellow'},
                        {'name': 'Accepted', 'color': 'green'},
                        {'name': 'Rejected', 'color': 'red'},
                        {'name': 'Waitlisted', 'color': 'orange'}
                    ]
                }
            },
            'Event Type': {
                'select': {
                    'options': [
                        {'name': 'Conference', 'color': 'blue'},
                        {'name': 'Festival', 'color': 'purple'},
                        {'name': 'Showcase', 'color': 'green'},
                        {'name': 'Awards', 'color': 'yellow'},
                        {'name': 'Press Event', 'color': 'red'}
                    ]
                }
            },
            'Platform': {
                'select': {
                    'options': [
                        {'name': 'Steam Next Fest', 'color': 'blue'},
                        {'name': 'PAX', 'color': 'green'},
                        {'name': 'GDC', 'color': 'orange'},
                        {'name': 'Gamescom', 'color': 'purple'},
                        {'name': 'E3', 'color': 'red'},
                        {'name': 'Other', 'color': 'gray'}
                    ]
                }
            },
            'Contact': {'rich_text': {}},
            'Application URL': {'url': {}},
            'Notes': {'rich_text': {}},
            'Priority': {
                'select': {
                    'options': [
                        {'name': 'High', 'color': 'red'},
                        {'name': 'Medium', 'color': 'yellow'},
                        {'name': 'Low', 'color': 'gray'}
                    ]
                }
            }
        }

        databases['events'] = self.create_database(
            'Events & Applications', 
            events_properties, 
            self.parent_page_id
        )

        # Generate environment variables for .env file
        print("\n" + "="*50)
        print("📝 ADD THESE TO YOUR .env FILE:")
        print("="*50)
        for key, db_id in databases.items():
            if db_id:
                env_key = f"{key.upper()}_DB_ID"
                if key == 'steam':
                    env_key = 'STEAM_WISHLIST_DB_ID'
                elif key == 'influencer':
                    env_key = 'INFLUENCER_DB_ID'
                elif key == 'events':
                    env_key = 'EVENTS_DB_ID'
                else:
                    env_key = f"{key.upper()}_DB_ID"
                print(f"{env_key}={db_id}")

        return databases

if __name__ == "__main__":
    creator = NotionDashboardCreator()
    creator.create_all_databases()
