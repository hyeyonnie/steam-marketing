#!/usr/bin/env python3
"""
Client for interacting with the Notion API.
This module uses the official notion-client library to provide a simplified
interface for adding data to Notion databases.
"""

import os
import notion_client

class NotionClient:
    def __init__(self):
        """
        Initializes the Notion client using the token from environment variables.
        """
        self.notion = notion_client.Client(auth=os.getenv('NOTION_TOKEN'))
        print("Notion client initialized.")

    def add_row_to_database(self, database_id, properties):
        """
        Adds a new row (page) to a specified Notion database.

        Args:
            database_id (str): The ID of the Notion database.
            properties (dict): A dictionary representing the properties (columns) of the new row.
                               The structure must match the Notion API's requirements.
                               Example:
                               {
                                   'Name': {'title': [{'text': {'content': 'New Row'}}],
                                   'Value': {'number': 123}
                               }
        Returns:
            dict: The response from the Notion API upon successful creation, or None.
        """
        if not database_id:
            print(f"❌ Error: Database ID is missing. Cannot add row.")
            return None

        try:
            response = self.notion.pages.create(
                parent={"database_id": database_id},
                properties=properties
            )
            print(f"✅ Successfully added a new row to database {database_id}.")
            return response
        except notion_client.APIResponseError as e:
            print(f"❌ Notion API Error while adding row to {database_id}: {e}")
            return None
