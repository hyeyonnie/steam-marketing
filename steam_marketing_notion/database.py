import sqlite3
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any, List
from config.settings import settings

class DatabaseManager:
    def __init__(self, db_path: str = None):
        self.db_path = db_path or settings.database_path
        self.logger = logging.getLogger(__name__)
        self._ensure_db_directory()
        self._initialize_database()
    
    def _ensure_db_directory(self):
        db_dir = Path(self.db_path).parent
        db_dir.mkdir(parents=True, exist_ok=True)
    
    def _initialize_database(self):
        with self.get_connection() as conn:
            self._create_tables(conn)
    
    def get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def _create_tables(self, conn: sqlite3.Connection):
        cursor = conn.cursor()
        
        # Customer configurations table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customer_configs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id TEXT UNIQUE NOT NULL,
                notion_page_id TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'active'
            )
        """)
        
        # Social media connections table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS social_connections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id TEXT NOT NULL,
                platform TEXT NOT NULL,
                connection_data TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                last_sync TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES customer_configs (customer_id),
                UNIQUE(customer_id, platform)
            )
        """)
        
        # Twitter data table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS twitter_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id TEXT NOT NULL,
                user_id TEXT NOT NULL,
                username TEXT NOT NULL,
                followers_count INTEGER,
                following_count INTEGER,
                tweet_count INTEGER,
                collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES customer_configs (customer_id)
            )
        """)
        
        # Twitter tweets table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS twitter_tweets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id TEXT NOT NULL,
                tweet_id TEXT UNIQUE NOT NULL,
                user_id TEXT NOT NULL,
                text TEXT,
                created_at TIMESTAMP,
                retweet_count INTEGER DEFAULT 0,
                like_count INTEGER DEFAULT 0,
                reply_count INTEGER DEFAULT 0,
                quote_count INTEGER DEFAULT 0,
                collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES customer_configs (customer_id)
            )
        """)
        
        # YouTube data table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS youtube_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id TEXT NOT NULL,
                channel_id TEXT NOT NULL,
                channel_name TEXT,
                subscriber_count INTEGER,
                video_count INTEGER,
                view_count INTEGER,
                collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES customer_configs (customer_id)
            )
        """)
        
        # YouTube videos table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS youtube_videos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id TEXT NOT NULL,
                video_id TEXT UNIQUE NOT NULL,
                channel_id TEXT NOT NULL,
                title TEXT,
                description TEXT,
                published_at TIMESTAMP,
                view_count INTEGER DEFAULT 0,
                like_count INTEGER DEFAULT 0,
                comment_count INTEGER DEFAULT 0,
                duration TEXT,
                collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES customer_configs (customer_id)
            )
        """)
        
        # Steam data table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS steam_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id TEXT NOT NULL,
                app_id INTEGER NOT NULL,
                app_name TEXT,
                wishlist_count INTEGER,
                followers_count INTEGER,
                review_score REAL,
                review_count INTEGER,
                collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES customer_configs (customer_id)
            )
        """)
        
        # Daily performance summary table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS daily_performance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id TEXT NOT NULL,
                date DATE NOT NULL,
                platform TEXT NOT NULL,
                metrics TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES customer_configs (customer_id),
                UNIQUE(customer_id, date, platform)
            )
        """)
        
        # Press and events table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS press_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id TEXT NOT NULL,
                title TEXT NOT NULL,
                description TEXT,
                url TEXT,
                type TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                event_date DATE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES customer_configs (customer_id)
            )
        """)
        
        # Processing status table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS processing_status (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id TEXT NOT NULL,
                task_name TEXT NOT NULL,
                status TEXT NOT NULL,
                last_run TIMESTAMP,
                next_run TIMESTAMP,
                error_message TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id) REFERENCES customer_configs (customer_id),
                UNIQUE(customer_id, task_name)
            )
        """)
        
        conn.commit()
        self.logger.info("Database tables created successfully")
    
    # Customer management methods
    def add_customer(self, customer_id: str, notion_page_id: str) -> bool:
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO customer_configs (customer_id, notion_page_id)
                    VALUES (?, ?)
                """, (customer_id, notion_page_id))
                conn.commit()
                self.logger.info(f"Added customer: {customer_id}")
                return True
        except sqlite3.IntegrityError:
            self.logger.warning(f"Customer {customer_id} already exists")
            return False
        except Exception as e:
            self.logger.error(f"Error adding customer {customer_id}: {e}")
            return False
    
    def get_customer(self, customer_id: str) -> Optional[Dict[str, Any]]:
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM customer_configs WHERE customer_id = ?
                """, (customer_id,))
                row = cursor.fetchone()
                return dict(row) if row else None
        except Exception as e:
            self.logger.error(f"Error getting customer {customer_id}: {e}")
            return None
    
    def get_all_customers(self) -> List[Dict[str, Any]]:
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM customer_configs WHERE status = 'active'")
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
        except Exception as e:
            self.logger.error(f"Error getting all customers: {e}")
            return []
    
    # Social connections management
    def update_social_connection(self, customer_id: str, platform: str, 
                               connection_data: str, status: str = 'connected') -> bool:
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT OR REPLACE INTO social_connections 
                    (customer_id, platform, connection_data, status, last_sync, updated_at)
                    VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                """, (customer_id, platform, connection_data, status))
                conn.commit()
                self.logger.info(f"Updated {platform} connection for {customer_id}")
                return True
        except Exception as e:
            self.logger.error(f"Error updating {platform} connection for {customer_id}: {e}")
            return False
    
    def get_social_connections(self, customer_id: str) -> List[Dict[str, Any]]:
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM social_connections WHERE customer_id = ?
                """, (customer_id,))
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
        except Exception as e:
            self.logger.error(f"Error getting social connections for {customer_id}: {e}")
            return []
    
    # Data storage methods
    def store_twitter_data(self, customer_id: str, user_data: Dict[str, Any]) -> bool:
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO twitter_data 
                    (customer_id, user_id, username, followers_count, following_count, tweet_count)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    customer_id,
                    user_data.get('id'),
                    user_data.get('username'),
                    user_data.get('public_metrics', {}).get('followers_count'),
                    user_data.get('public_metrics', {}).get('following_count'),
                    user_data.get('public_metrics', {}).get('tweet_count')
                ))
                conn.commit()
                return True
        except Exception as e:
            self.logger.error(f"Error storing Twitter data for {customer_id}: {e}")
            return False
    
    def store_twitter_tweets(self, customer_id: str, tweets: List[Dict[str, Any]]) -> bool:
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                for tweet in tweets:
                    cursor.execute("""
                        INSERT OR REPLACE INTO twitter_tweets 
                        (customer_id, tweet_id, user_id, text, created_at, 
                         retweet_count, like_count, reply_count, quote_count)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        customer_id,
                        tweet.get('id'),
                        tweet.get('author_id'),
                        tweet.get('text'),
                        tweet.get('created_at'),
                        tweet.get('public_metrics', {}).get('retweet_count', 0),
                        tweet.get('public_metrics', {}).get('like_count', 0),
                        tweet.get('public_metrics', {}).get('reply_count', 0),
                        tweet.get('public_metrics', {}).get('quote_count', 0)
                    ))
                conn.commit()
                return True
        except Exception as e:
            self.logger.error(f"Error storing Twitter tweets for {customer_id}: {e}")
            return False
    
    def store_youtube_data(self, customer_id: str, channel_data: Dict[str, Any]) -> bool:
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                statistics = channel_data.get('statistics', {})
                cursor.execute("""
                    INSERT INTO youtube_data 
                    (customer_id, channel_id, channel_name, subscriber_count, video_count, view_count)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    customer_id,
                    channel_data.get('id'),
                    channel_data.get('snippet', {}).get('title'),
                    int(statistics.get('subscriberCount', 0)),
                    int(statistics.get('videoCount', 0)),
                    int(statistics.get('viewCount', 0))
                ))
                conn.commit()
                return True
        except Exception as e:
            self.logger.error(f"Error storing YouTube data for {customer_id}: {e}")
            return False
    
    def store_steam_data(self, customer_id: str, app_data: Dict[str, Any]) -> bool:
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO steam_data 
                    (customer_id, app_id, app_name, wishlist_count, followers_count)
                    VALUES (?, ?, ?, ?, ?)
                """, (
                    customer_id,
                    app_data.get('steam_appid'),
                    app_data.get('name'),
                    app_data.get('wishlist_count', 0),
                    app_data.get('followers_count', 0)
                ))
                conn.commit()
                return True
        except Exception as e:
            self.logger.error(f"Error storing Steam data for {customer_id}: {e}")
            return False
    
    # Processing status management
    def update_processing_status(self, customer_id: str, task_name: str, 
                               status: str, error_message: str = None) -> bool:
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT OR REPLACE INTO processing_status 
                    (customer_id, task_name, status, last_run, error_message, updated_at)
                    VALUES (?, ?, ?, CURRENT_TIMESTAMP, ?, CURRENT_TIMESTAMP)
                """, (customer_id, task_name, status, error_message))
                conn.commit()
                return True
        except Exception as e:
            self.logger.error(f"Error updating processing status: {e}")
            return False
    
    def cleanup_old_data(self, days: int = 90) -> bool:
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                
                # Clean up old daily performance data
                cursor.execute("""
                    DELETE FROM daily_performance 
                    WHERE created_at < datetime('now', '-{} days')
                """.format(days))
                
                # Clean up old tweets (keep last 30 days)
                cursor.execute("""
                    DELETE FROM twitter_tweets 
                    WHERE collected_at < datetime('now', '-30 days')
                """)
                
                # Clean up old videos (keep last 30 days)
                cursor.execute("""
                    DELETE FROM youtube_videos 
                    WHERE collected_at < datetime('now', '-30 days')
                """)
                
                conn.commit()
                self.logger.info(f"Cleaned up data older than {days} days")
                return True
        except Exception as e:
            self.logger.error(f"Error cleaning up old data: {e}")
            return False

# Global database instance
db = DatabaseManager()