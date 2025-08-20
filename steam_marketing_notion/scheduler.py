import logging
import sys
import signal
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from config.settings import settings
from database import db
from collectors import twitter_collector, youtube_collector, steam_collector, web_scraper
from processors import data_processor, metrics_calculator
from notion.customer_config import customer_config_monitor

class MarketingScheduler:
    def __init__(self):
        self.logger = self._setup_logging()
        self.scheduler = BlockingScheduler()
        self.schedule_config = settings.get_schedule_config()
        self._setup_signal_handlers()
        self._setup_jobs()
    
    def _setup_logging(self):
        logging_config = settings.get_logging_config()
        
        logging.basicConfig(
            level=getattr(logging, logging_config.get('level', 'INFO')),
            format=logging_config.get('format', '%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
            handlers=[
                logging.FileHandler(settings.log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        
        return logging.getLogger(__name__)
    
    def _setup_signal_handlers(self):
        def signal_handler(signum, frame):
            self.logger.info(f"Received signal {signum}, shutting down scheduler...")
            self.shutdown()
            sys.exit(0)
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
    
    def _setup_jobs(self):
        try:
            # Daily data collection job (2:00 AM)
            daily_time = self.schedule_config.get('daily_collection_time', '02:00')
            hour, minute = daily_time.split(':')
            
            self.scheduler.add_job(
                func=self.daily_data_collection,
                trigger=CronTrigger(hour=int(hour), minute=int(minute)),
                id='daily_collection',
                name='Daily Data Collection',
                misfire_grace_time=300
            )
            
            # Weekly data collection job (Sunday 3:00 AM)
            weekly_time = self.schedule_config.get('weekly_collection_time', '03:00')
            weekly_hour, weekly_minute = weekly_time.split(':')
            
            self.scheduler.add_job(
                func=self.weekly_data_collection,
                trigger=CronTrigger(day_of_week='sun', hour=int(weekly_hour), minute=int(weekly_minute)),
                id='weekly_collection',
                name='Weekly Data Collection',
                misfire_grace_time=300
            )
            
            # Customer configuration monitoring (every 5 minutes)
            check_interval = self.schedule_config.get('customer_config_check_interval', 300)
            
            self.scheduler.add_job(
                func=self.monitor_customer_configs,
                trigger=IntervalTrigger(seconds=check_interval),
                id='config_monitoring',
                name='Customer Config Monitoring',
                misfire_grace_time=60
            )
            
            # Database cleanup job (weekly, Sunday 4:00 AM)
            self.scheduler.add_job(
                func=self.cleanup_old_data,
                trigger=CronTrigger(day_of_week='sun', hour=4, minute=0),
                id='database_cleanup',
                name='Database Cleanup',
                misfire_grace_time=300
            )
            
            # Health check job (every hour)
            self.scheduler.add_job(
                func=self.health_check,
                trigger=IntervalTrigger(hours=1),
                id='health_check',
                name='System Health Check',
                misfire_grace_time=60
            )
            
            self.logger.info("Scheduler jobs configured successfully")
            
        except Exception as e:
            self.logger.error(f"Error setting up scheduler jobs: {e}")
    
    def daily_data_collection(self):
        try:
            self.logger.info("Starting daily data collection...")
            
            # Collect Twitter data
            self.logger.info("Collecting Twitter data...")
            twitter_results = twitter_collector.collect_all_customers()
            self.logger.info(f"Twitter collection results: {sum(twitter_results.values())} successful")
            
            # Collect YouTube data
            self.logger.info("Collecting YouTube data...")
            youtube_results = youtube_collector.collect_all_customers()
            self.logger.info(f"YouTube collection results: {sum(youtube_results.values())} successful")
            
            # Collect Steam data
            self.logger.info("Collecting Steam data...")
            steam_results = steam_collector.collect_all_customers()
            self.logger.info(f"Steam collection results: {sum(steam_results.values())} successful")
            
            # Process and calculate daily summaries
            self.logger.info("Processing daily summaries...")
            self.process_daily_summaries()
            
            # Update Notion dashboards
            self.logger.info("Updating Notion dashboards...")
            self.update_notion_dashboards()
            
            self.logger.info("Daily data collection completed successfully")
            
        except Exception as e:
            self.logger.error(f"Error in daily data collection: {e}")
    
    def weekly_data_collection(self):
        try:
            self.logger.info("Starting weekly data collection...")
            
            # Collect press and influencer mentions
            self.logger.info("Collecting press and influencer data...")
            press_results = web_scraper.collect_all_customers()
            self.logger.info(f"Press collection results: {sum(press_results.values())} successful")
            
            # Generate weekly reports
            self.logger.info("Generating weekly reports...")
            self.generate_weekly_reports()
            
            self.logger.info("Weekly data collection completed successfully")
            
        except Exception as e:
            self.logger.error(f"Error in weekly data collection: {e}")
    
    def monitor_customer_configs(self):
        try:
            self.logger.debug("Monitoring customer configurations...")
            
            # Check for new or updated customer configurations
            updated_configs = customer_config_monitor.check_for_updates()
            
            if updated_configs:
                self.logger.info(f"Found {len(updated_configs)} configuration updates")
                
                for customer_id, config_data in updated_configs.items():
                    try:
                        # Process the configuration update
                        success = customer_config_monitor.process_config_update(customer_id, config_data)
                        
                        if success:
                            self.logger.info(f"Successfully processed config update for {customer_id}")
                        else:
                            self.logger.warning(f"Failed to process config update for {customer_id}")
                            
                    except Exception as e:
                        self.logger.error(f"Error processing config for {customer_id}: {e}")
            
        except Exception as e:
            self.logger.error(f"Error in customer config monitoring: {e}")
    
    def process_daily_summaries(self):
        try:
            customers = db.get_all_customers()
            today = datetime.now().strftime('%Y-%m-%d')
            
            for customer in customers:
                customer_id = customer['customer_id']
                
                try:
                    # Calculate daily summary
                    summary = metrics_calculator.calculate_daily_summary(customer_id, today)
                    
                    if summary:
                        # Store in database
                        success = metrics_calculator.store_daily_summary(customer_id, summary)
                        
                        if success:
                            self.logger.info(f"Processed daily summary for {customer_id}")
                        else:
                            self.logger.warning(f"Failed to store daily summary for {customer_id}")
                    
                except Exception as e:
                    self.logger.error(f"Error processing daily summary for {customer_id}: {e}")
            
        except Exception as e:
            self.logger.error(f"Error in process_daily_summaries: {e}")
    
    def update_notion_dashboards(self):
        try:
            # This would be implemented in notion/database_updater.py
            self.logger.info("Notion dashboard updates would be implemented here")
            
        except Exception as e:
            self.logger.error(f"Error updating Notion dashboards: {e}")
    
    def generate_weekly_reports(self):
        try:
            customers = db.get_all_customers()
            
            for customer in customers:
                customer_id = customer['customer_id']
                
                try:
                    # Calculate weekly summary
                    weekly_summary = metrics_calculator.calculate_weekly_summary(customer_id)
                    
                    if weekly_summary:
                        self.logger.info(f"Generated weekly report for {customer_id}")
                    
                except Exception as e:
                    self.logger.error(f"Error generating weekly report for {customer_id}: {e}")
            
        except Exception as e:
            self.logger.error(f"Error in generate_weekly_reports: {e}")
    
    def cleanup_old_data(self):
        try:
            self.logger.info("Starting database cleanup...")
            
            # Clean up old data (default: 90 days)
            success = db.cleanup_old_data(90)
            
            if success:
                self.logger.info("Database cleanup completed successfully")
            else:
                self.logger.warning("Database cleanup encountered issues")
            
        except Exception as e:
            self.logger.error(f"Error in database cleanup: {e}")
    
    def health_check(self):
        try:
            self.logger.debug("Performing system health check...")
            
            health_status = {
                'timestamp': datetime.now().isoformat(),
                'database': self._check_database_health(),
                'apis': self._check_api_health(),
                'scheduler': True
            }
            
            # Log any issues
            issues = []
            for component, status in health_status.items():
                if component != 'timestamp' and not status:
                    issues.append(component)
            
            if issues:
                self.logger.warning(f"Health check issues detected: {', '.join(issues)}")
            else:
                self.logger.debug("All systems healthy")
            
        except Exception as e:
            self.logger.error(f"Error in health check: {e}")
    
    def _check_database_health(self) -> bool:
        try:
            # Test database connection
            with db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 1")
                return True
        except:
            return False
    
    def _check_api_health(self) -> Dict[str, bool]:
        try:
            return {
                'twitter': twitter_collector.test_connection(),
                'youtube': youtube_collector.test_connection(),
                'steam': steam_collector.test_connection(),
                'notion': True  # Would implement notion test
            }
        except:
            return {
                'twitter': False,
                'youtube': False,
                'steam': False,
                'notion': False
            }
    
    def start(self):
        try:
            self.logger.info("Starting Marketing Scheduler...")
            self.logger.info(f"Scheduled jobs: {len(self.scheduler.get_jobs())}")
            
            for job in self.scheduler.get_jobs():
                self.logger.info(f"  - {job.name} (ID: {job.id}) - Next run: {job.next_run_time}")
            
            self.scheduler.start()
            
        except Exception as e:
            self.logger.error(f"Error starting scheduler: {e}")
            raise
    
    def shutdown(self):
        try:
            self.logger.info("Shutting down scheduler...")
            self.scheduler.shutdown(wait=True)
            self.logger.info("Scheduler shutdown complete")
            
        except Exception as e:
            self.logger.error(f"Error shutting down scheduler: {e}")
    
    def add_manual_job(self, job_name: str, customer_id: str = None):
        try:
            if job_name == 'daily_collection':
                if customer_id:
                    self.logger.info(f"Running manual data collection for {customer_id}")
                    # Implement single customer collection
                else:
                    self.logger.info("Running manual daily data collection for all customers")
                    self.daily_data_collection()
            
            elif job_name == 'weekly_collection':
                self.logger.info("Running manual weekly data collection")
                self.weekly_data_collection()
            
            else:
                self.logger.warning(f"Unknown manual job: {job_name}")
            
        except Exception as e:
            self.logger.error(f"Error in manual job {job_name}: {e}")

def main():
    try:
        # Validate configuration
        credentials = settings.validate_credentials()
        missing_creds = [platform for platform, valid in credentials.items() if not valid]
        
        if missing_creds:
            logging.warning(f"Missing credentials for: {', '.join(missing_creds)}")
        
        # Initialize and start scheduler
        scheduler = MarketingScheduler()
        scheduler.start()
        
    except KeyboardInterrupt:
        logging.info("Received interrupt signal, shutting down...")
    except Exception as e:
        logging.error(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()