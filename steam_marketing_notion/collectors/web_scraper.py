import requests
import logging
import time
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from config.settings import settings
from database import db

class WebScraper:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # Common gaming/tech press sites
        self.press_sites = [
            'ign.com',
            'gamespot.com',
            'polygon.com',
            'kotaku.com',
            'techcrunch.com',
            'gamasutra.com',
            'rockpapershotgun.com',
            'pcgamer.com',
            'destructoid.com',
            'gamesindustry.biz'
        ]
        
        # Social platforms for influencer monitoring
        self.social_platforms = [
            'twitch.tv',
            'tiktok.com',
            'instagram.com'
        ]
    
    def search_google_news(self, query: str, days_back: int = 7) -> List[Dict[str, Any]]:
        try:
            # Using Google News RSS (public and free)
            from_date = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')
            
            # Google News RSS search
            url = "https://news.google.com/rss/search"
            params = {
                'q': f'{query} after:{from_date}',
                'hl': 'en-US',
                'gl': 'US',
                'ceid': 'US:en'
            }
            
            response = self.session.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'xml')
                items = soup.find_all('item')
                
                articles = []
                for item in items:
                    article = {
                        'title': item.title.text if item.title else '',
                        'link': item.link.text if item.link else '',
                        'description': item.description.text if item.description else '',
                        'pub_date': item.pubDate.text if item.pubDate else '',
                        'source': self._extract_source_from_link(item.link.text if item.link else ''),
                        'type': 'press'
                    }
                    articles.append(article)
                
                self.logger.info(f"Found {len(articles)} articles for query: {query}")
                return articles
            
            return []
            
        except Exception as e:
            self.logger.error(f"Error searching Google News for {query}: {e}")
            return []
    
    def search_reddit(self, subreddit: str, query: str, days_back: int = 7) -> List[Dict[str, Any]]:
        try:
            # Using Reddit's JSON API (public)
            url = f"https://www.reddit.com/r/{subreddit}/search.json"
            params = {
                'q': query,
                'sort': 'new',
                'restrict_sr': 'on',
                'limit': 25,
                't': 'week' if days_back <= 7 else 'month'
            }
            
            response = self.session.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                posts = data.get('data', {}).get('children', [])
                
                results = []
                for post in posts:
                    post_data = post.get('data', {})
                    created_time = datetime.fromtimestamp(post_data.get('created_utc', 0))
                    
                    # Filter by date
                    if created_time >= datetime.now() - timedelta(days=days_back):
                        result = {
                            'title': post_data.get('title', ''),
                            'link': f"https://reddit.com{post_data.get('permalink', '')}",
                            'description': post_data.get('selftext', '')[:500] + '...' if len(post_data.get('selftext', '')) > 500 else post_data.get('selftext', ''),
                            'score': post_data.get('score', 0),
                            'comments': post_data.get('num_comments', 0),
                            'author': post_data.get('author', ''),
                            'subreddit': subreddit,
                            'created_time': created_time.isoformat(),
                            'type': 'social',
                            'platform': 'reddit'
                        }
                        results.append(result)
                
                self.logger.info(f"Found {len(results)} Reddit posts in r/{subreddit} for: {query}")
                return results
            
            return []
            
        except Exception as e:
            self.logger.error(f"Error searching Reddit r/{subreddit} for {query}: {e}")
            return []
    
    def monitor_twitch_category(self, game_name: str) -> List[Dict[str, Any]]:
        try:
            # This would require Twitch API credentials
            # For now, return placeholder structure
            self.logger.info(f"Twitch monitoring for {game_name} requires API setup")
            
            return [{
                'title': f"Twitch streams for {game_name}",
                'link': f"https://www.twitch.tv/directory/game/{game_name.replace(' ', '%20')}",
                'description': 'Monitor Twitch streams manually or set up Twitch API integration',
                'type': 'influencer',
                'platform': 'twitch',
                'status': 'requires_api_setup'
            }]
            
        except Exception as e:
            self.logger.error(f"Error monitoring Twitch for {game_name}: {e}")
            return []
    
    def search_youtube_mentions(self, query: str, days_back: int = 7) -> List[Dict[str, Any]]:
        try:
            # This integrates with the YouTube collector
            from collectors.youtube_collector import youtube_collector
            
            if not youtube_collector.youtube_service:
                return []
            
            # Calculate date range
            published_after = (datetime.now() - timedelta(days=days_back)).isoformat() + 'Z'
            
            # Search for videos mentioning the query
            request = youtube_collector.youtube_service.search().list(
                part="snippet",
                q=query,
                publishedAfter=published_after,
                order="relevance",
                type="video",
                maxResults=20
            )
            response = request.execute()
            
            videos = []
            for item in response.get('items', []):
                video = {
                    'title': item['snippet']['title'],
                    'link': f"https://www.youtube.com/watch?v={item['id']['videoId']}",
                    'description': item['snippet']['description'][:500] + '...' if len(item['snippet']['description']) > 500 else item['snippet']['description'],
                    'channel': item['snippet']['channelTitle'],
                    'published_at': item['snippet']['publishedAt'],
                    'thumbnail': item['snippet']['thumbnails'].get('default', {}).get('url', ''),
                    'type': 'influencer',
                    'platform': 'youtube'
                }
                videos.append(video)
            
            self.logger.info(f"Found {len(videos)} YouTube videos for: {query}")
            return videos
            
        except Exception as e:
            self.logger.error(f"Error searching YouTube for {query}: {e}")
            return []
    
    def scrape_specific_sites(self, query: str, sites: List[str] = None) -> List[Dict[str, Any]]:
        try:
            target_sites = sites or self.press_sites[:5]  # Limit to avoid being blocked
            results = []
            
            for site in target_sites:
                try:
                    # Use site-specific search (most sites have search URLs)
                    search_url = f"https://{site}/search?q={query}"
                    
                    response = self.session.get(search_url, timeout=10)
                    
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.content, 'html.parser')
                        
                        # Generic article extraction (varies by site)
                        articles = self._extract_articles_generic(soup, site)
                        
                        for article in articles[:3]:  # Limit per site
                            article['source'] = site
                            article['type'] = 'press'
                            results.append(article)
                    
                    # Be respectful with rate limiting
                    time.sleep(2)
                    
                except Exception as site_error:
                    self.logger.warning(f"Error scraping {site}: {site_error}")
                    continue
            
            self.logger.info(f"Scraped {len(results)} articles from {len(target_sites)} sites")
            return results
            
        except Exception as e:
            self.logger.error(f"Error scraping sites for {query}: {e}")
            return []
    
    def _extract_articles_generic(self, soup: BeautifulSoup, site: str) -> List[Dict[str, Any]]:
        articles = []
        
        try:
            # Common article selectors (varies by site)
            article_selectors = [
                'article',
                '.article',
                '.post',
                '.entry',
                '.story',
                '[data-article]'
            ]
            
            title_selectors = [
                'h1', 'h2', 'h3',
                '.title',
                '.headline',
                '.article-title'
            ]
            
            link_selectors = [
                'a[href*="/"]'
            ]
            
            for selector in article_selectors:
                elements = soup.select(selector)
                
                for element in elements[:5]:  # Limit per selector
                    title = ''
                    link = ''
                    description = ''
                    
                    # Try to find title
                    for title_sel in title_selectors:
                        title_elem = element.select_one(title_sel)
                        if title_elem:
                            title = title_elem.get_text(strip=True)
                            break
                    
                    # Try to find link
                    link_elem = element.select_one('a[href]')
                    if link_elem:
                        href = link_elem.get('href')
                        if href:
                            if href.startswith('/'):
                                link = f"https://{site}{href}"
                            elif href.startswith('http'):
                                link = href
                    
                    # Try to find description
                    desc_elem = element.select_one('p, .description, .excerpt')
                    if desc_elem:
                        description = desc_elem.get_text(strip=True)[:300]
                    
                    if title and link:
                        articles.append({
                            'title': title,
                            'link': link,
                            'description': description,
                            'scraped_at': datetime.now().isoformat()
                        })
                
                if articles:  # If we found articles, stop trying other selectors
                    break
            
        except Exception as e:
            self.logger.error(f"Error extracting articles from {site}: {e}")
        
        return articles
    
    def _extract_source_from_link(self, link: str) -> str:
        try:
            parsed = urlparse(link)
            domain = parsed.netloc.lower()
            
            # Clean up domain
            if domain.startswith('www.'):
                domain = domain[4:]
            
            return domain
        except:
            return 'unknown'
    
    def collect_mentions(self, customer_id: str, game_name: str, company_name: str = None) -> bool:
        try:
            all_results = []
            search_terms = [game_name]
            
            if company_name:
                search_terms.append(company_name)
            
            for term in search_terms:
                # Search Google News
                news_results = self.search_google_news(term, days_back=7)
                all_results.extend(news_results)
                
                # Search relevant subreddits
                gaming_subreddits = ['gaming', 'Games', 'IndieGaming', 'gamedev']
                for subreddit in gaming_subreddits:
                    reddit_results = self.search_reddit(subreddit, term, days_back=7)
                    all_results.extend(reddit_results)
                
                # Search YouTube
                youtube_results = self.search_youtube_mentions(term, days_back=7)
                all_results.extend(youtube_results)
                
                # Rate limiting between searches
                time.sleep(1)
            
            # Store results in database
            if all_results:
                success = self._store_press_mentions(customer_id, all_results)
                if success:
                    self.logger.info(f"Stored {len(all_results)} mentions for {customer_id}")
                    return True
            
            return False
            
        except Exception as e:
            self.logger.error(f"Error collecting mentions for {customer_id}: {e}")
            return False
    
    def _store_press_mentions(self, customer_id: str, mentions: List[Dict[str, Any]]) -> bool:
        try:
            with db.get_connection() as conn:
                cursor = conn.cursor()
                
                for mention in mentions:
                    cursor.execute("""
                        INSERT OR REPLACE INTO press_events 
                        (customer_id, title, description, url, type, status, created_at)
                        VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                    """, (
                        customer_id,
                        mention.get('title', ''),
                        mention.get('description', ''),
                        mention.get('link', ''),
                        mention.get('type', 'mention'),
                        'detected'
                    ))
                
                conn.commit()
                return True
                
        except Exception as e:
            self.logger.error(f"Error storing press mentions for {customer_id}: {e}")
            return False
    
    def collect_all_customers(self) -> Dict[str, bool]:
        results = {}
        customers = db.get_all_customers()
        
        for customer in customers:
            customer_id = customer['customer_id']
            
            try:
                # Get customer's game information from Steam data
                with db.get_connection() as conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        SELECT app_name FROM steam_data 
                        WHERE customer_id = ? 
                        ORDER BY collected_at DESC 
                        LIMIT 1
                    """, (customer_id,))
                    
                    result = cursor.fetchone()
                    game_name = result[0] if result else f"Customer {customer_id} Game"
                
                # Collect mentions
                success = self.collect_mentions(customer_id, game_name)
                results[customer_id] = success
                
                # Update processing status
                status = 'completed' if success else 'failed'
                db.update_processing_status(customer_id, 'press_monitoring', status)
                
                # Rate limiting between customers
                time.sleep(5)
                
            except Exception as e:
                self.logger.error(f"Error processing customer {customer_id}: {e}")
                results[customer_id] = False
                db.update_processing_status(customer_id, 'press_monitoring', 'failed', str(e))
        
        return results
    
    def get_mentions_summary(self, customer_id: str, days: int = 7) -> Dict[str, Any]:
        try:
            with db.get_connection() as conn:
                cursor = conn.cursor()
                
                cursor.execute("""
                    SELECT 
                        type,
                        COUNT(*) as count,
                        GROUP_CONCAT(title, ' | ') as titles
                    FROM press_events 
                    WHERE customer_id = ? 
                    AND created_at >= datetime('now', '-{} days')
                    GROUP BY type
                """.format(days), (customer_id,))
                
                results = cursor.fetchall()
                
                summary = {
                    'period_days': days,
                    'total_mentions': 0,
                    'by_type': {},
                    'recent_titles': []
                }
                
                for result in results:
                    mention_type = result[0]
                    count = result[1]
                    titles = result[2].split(' | ')[:5] if result[2] else []
                    
                    summary['total_mentions'] += count
                    summary['by_type'][mention_type] = count
                    summary['recent_titles'].extend(titles)
                
                return summary
                
        except Exception as e:
            self.logger.error(f"Error getting mentions summary for {customer_id}: {e}")
            return {}

# Global instance
web_scraper = WebScraper()