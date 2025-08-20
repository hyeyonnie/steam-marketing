import logging
import json
from datetime import datetime
from typing import Dict, List, Any, Optional
from notion_client import Client
from config.api_config import api_config
from config.settings import settings

class NotionClient:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.client = None
        self.rate_limit = api_config.get_rate_limit('notion')
        self._initialize_client()
    
    def _initialize_client(self):
        try:
            notion_config = api_config.get_notion_config()
            
            if not notion_config.get('api_key'):
                self.logger.error("Notion API key not configured")
                return
            
            self.client = Client(auth=notion_config['api_key'])
            self.logger.info("Notion client initialized successfully")
            
        except Exception as e:
            self.logger.error(f"Failed to initialize Notion client: {e}")
    
    def test_connection(self, api_key: str = None) -> bool:
        try:
            test_key = api_key or api_config.get_notion_config().get('api_key')
            
            if not test_key:
                return False
            
            test_client = Client(auth=test_key)
            
            # Test with a simple API call
            users = test_client.users.list()
            
            if users and 'results' in users:
                self.logger.info("Notion API connection test successful")
                return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"Notion API connection test failed: {e}")
            return False
    
    def create_database(self, parent_page_id: str, title: str, properties: Dict[str, Any]) -> Optional[str]:
        try:
            if not self.client:
                return None
            
            database = self.client.databases.create(
                parent={
                    "type": "page_id",
                    "page_id": parent_page_id
                },
                title=[
                    {
                        "type": "text",
                        "text": {
                            "content": title
                        }
                    }
                ],
                properties=properties
            )
            
            self.logger.info(f"Created database: {title}")
            return database['id']
            
        except Exception as e:
            self.logger.error(f"Error creating database {title}: {e}")
            return None
    
    def query_database(self, database_id: str, filter_conditions: Dict[str, Any] = None, sorts: List[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        try:
            if not self.client:
                return []
            
            query_params = {"database_id": database_id}
            
            if filter_conditions:
                query_params["filter"] = filter_conditions
            
            if sorts:
                query_params["sorts"] = sorts
            
            response = self.client.databases.query(**query_params)
            
            return response.get('results', [])
            
        except Exception as e:
            self.logger.error(f"Error querying database {database_id}: {e}")
            return []
    
    def create_page(self, parent_id: str, properties: Dict[str, Any], children: List[Dict[str, Any]] = None) -> Optional[str]:
        try:
            if not self.client:
                return None
            
            page_data = {
                "parent": {"database_id": parent_id},
                "properties": properties
            }
            
            if children:
                page_data["children"] = children
            
            page = self.client.pages.create(**page_data)
            
            self.logger.info(f"Created page in database {parent_id}")
            return page['id']
            
        except Exception as e:
            self.logger.error(f"Error creating page in {parent_id}: {e}")
            return None
    
    def update_page(self, page_id: str, properties: Dict[str, Any]) -> bool:
        try:
            if not self.client:
                return False
            
            self.client.pages.update(
                page_id=page_id,
                properties=properties
            )
            
            self.logger.info(f"Updated page {page_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error updating page {page_id}: {e}")
            return False
    
    def append_blocks(self, page_id: str, blocks: List[Dict[str, Any]]) -> bool:
        try:
            if not self.client:
                return False
            
            self.client.blocks.children.append(
                block_id=page_id,
                children=blocks
            )
            
            self.logger.info(f"Appended {len(blocks)} blocks to page {page_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error appending blocks to {page_id}: {e}")
            return False
    
    def get_page(self, page_id: str) -> Optional[Dict[str, Any]]:
        try:
            if not self.client:
                return None
            
            page = self.client.pages.retrieve(page_id=page_id)
            return page
            
        except Exception as e:
            self.logger.error(f"Error getting page {page_id}: {e}")
            return None
    
    def get_database(self, database_id: str) -> Optional[Dict[str, Any]]:
        try:
            if not self.client:
                return None
            
            database = self.client.databases.retrieve(database_id=database_id)
            return database
            
        except Exception as e:
            self.logger.error(f"Error getting database {database_id}: {e}")
            return None
    
    def search_pages(self, query: str = "", filter_conditions: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        try:
            if not self.client:
                return []
            
            search_params = {}
            
            if query:
                search_params["query"] = query
            
            if filter_conditions:
                search_params["filter"] = filter_conditions
            
            response = self.client.search(**search_params)
            
            return response.get('results', [])
            
        except Exception as e:
            self.logger.error(f"Error searching pages: {e}")
            return []
    
    def create_text_block(self, text: str, is_bold: bool = False, is_italic: bool = False) -> Dict[str, Any]:
        return {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": text
                        },
                        "annotations": {
                            "bold": is_bold,
                            "italic": is_italic
                        }
                    }
                ]
            }
        }
    
    def create_heading_block(self, text: str, level: int = 1) -> Dict[str, Any]:
        heading_types = {1: "heading_1", 2: "heading_2", 3: "heading_3"}
        heading_type = heading_types.get(level, "heading_2")
        
        return {
            "object": "block",
            "type": heading_type,
            heading_type: {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": text
                        }
                    }
                ]
            }
        }
    
    def create_callout_block(self, text: str, emoji: str = "📊", color: str = "blue") -> Dict[str, Any]:
        return {
            "object": "block",
            "type": "callout",
            "callout": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": text
                        }
                    }
                ],
                "icon": {
                    "type": "emoji",
                    "emoji": emoji
                },
                "color": color
            }
        }
    
    def create_table_block(self, headers: List[str], rows: List[List[str]]) -> Dict[str, Any]:
        table_rows = []
        
        # Add header row
        header_cells = []
        for header in headers:
            header_cells.append({
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": header
                        },
                        "annotations": {
                            "bold": True
                        }
                    }
                ]
            })
        
        table_rows.append({
            "type": "table_row",
            "table_row": {
                "cells": header_cells
            }
        })
        
        # Add data rows
        for row in rows:
            row_cells = []
            for cell in row:
                row_cells.append({
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": str(cell)
                            }
                        }
                    ]
                })
            
            table_rows.append({
                "type": "table_row",
                "table_row": {
                    "cells": row_cells
                }
            })
        
        return {
            "object": "block",
            "type": "table",
            "table": {
                "table_width": len(headers),
                "has_column_header": True,
                "has_row_header": False,
                "children": table_rows
            }
        }
    
    def create_bulleted_list_block(self, items: List[str]) -> List[Dict[str, Any]]:
        blocks = []
        
        for item in items:
            blocks.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": item
                            }
                        }
                    ]
                }
            })
        
        return blocks
    
    def format_metric_with_trend(self, current: int, previous: int, metric_name: str) -> str:
        if previous == 0:
            return f"{metric_name}: {current:,}"
        
        change = current - previous
        change_percent = (change / previous) * 100
        
        if change > 0:
            trend = f"↗️ +{change:,} (+{change_percent:.1f}%)"
        elif change < 0:
            trend = f"↘️ {change:,} ({change_percent:.1f}%)"
        else:
            trend = "→ No change"
        
        return f"{metric_name}: {current:,} {trend}"
    
    def create_metric_callout(self, title: str, value: str, trend: str = "", emoji: str = "📈") -> Dict[str, Any]:
        content = f"**{title}**\n{value}"
        if trend:
            content += f"\n{trend}"
        
        return self.create_callout_block(content, emoji)

# Global instance
notion_client = NotionClient()