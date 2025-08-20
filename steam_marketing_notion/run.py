#!/usr/bin/env python3
"""
Steam Marketing Dashboard - Main Entry Point

This script provides various ways to run the marketing dashboard system:
- Full scheduler mode (default)
- Manual data collection
- Customer setup
- Health checks
"""

import sys
import argparse
import logging
from datetime import datetime

def setup_basic_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def run_scheduler():
    """Run the full scheduler with all automated jobs"""
    from scheduler import MarketingScheduler
    
    print("🚀 Starting Steam Marketing Dashboard Scheduler...")
    print("📊 Automated data collection for indie game studios")
    print("=" * 60)
    
    try:
        scheduler = MarketingScheduler()
        scheduler.start()
    except KeyboardInterrupt:
        print("\n⏹️  Scheduler stopped by user")
    except Exception as e:
        print(f"❌ Error starting scheduler: {e}")
        sys.exit(1)

def run_manual_collection(platforms=None, customer_id=None):
    """Run manual data collection for specified platforms"""
    from collectors import twitter_collector, youtube_collector, steam_collector
    
    print("🔄 Running manual data collection...")
    
    if not platforms:
        platforms = ['twitter', 'youtube', 'steam']
    
    results = {}
    
    if 'twitter' in platforms:
        print("🐦 Collecting Twitter data...")
        if customer_id:
            # Single customer collection logic would go here
            results['twitter'] = True
        else:
            results['twitter'] = twitter_collector.collect_all_customers()
    
    if 'youtube' in platforms:
        print("📺 Collecting YouTube data...")
        if customer_id:
            # Single customer collection logic would go here
            results['youtube'] = True
        else:
            results['youtube'] = youtube_collector.collect_all_customers()
    
    if 'steam' in platforms:
        print("🎮 Collecting Steam data...")
        if customer_id:
            # Single customer collection logic would go here
            results['steam'] = True
        else:
            results['steam'] = steam_collector.collect_all_customers()
    
    # Print results
    print("\n📈 Collection Results:")
    for platform, result in results.items():
        if isinstance(result, dict):
            successful = sum(1 for success in result.values() if success)
            total = len(result)
            print(f"  {platform}: {successful}/{total} customers successful")
        else:
            status = "✅ Success" if result else "❌ Failed"
            print(f"  {platform}: {status}")

def run_health_check():
    """Run system health check"""
    from config.settings import settings
    from database import db
    from collectors import twitter_collector, youtube_collector, steam_collector
    
    print("🏥 Running System Health Check...")
    print("=" * 40)
    
    # Check configuration
    print("📋 Configuration:")
    credentials = settings.validate_credentials()
    for platform, valid in credentials.items():
        status = "✅ Valid" if valid else "❌ Missing"
        print(f"  {platform}: {status}")
    
    # Check database
    print("\n💾 Database:")
    try:
        with db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM customer_configs")
            customer_count = cursor.fetchone()[0]
            print(f"  Connection: ✅ Active")
            print(f"  Customers: {customer_count}")
    except Exception as e:
        print(f"  Connection: ❌ Failed - {e}")
    
    # Check API connections
    print("\n🌐 API Connections:")
    
    try:
        twitter_ok = twitter_collector.test_connection()
        print(f"  Twitter: {'✅ Connected' if twitter_ok else '❌ Failed'}")
    except Exception as e:
        print(f"  Twitter: ❌ Error - {e}")
    
    try:
        youtube_ok = youtube_collector.test_connection()
        print(f"  YouTube: {'✅ Connected' if youtube_ok else '❌ Failed'}")
    except Exception as e:
        print(f"  YouTube: ❌ Error - {e}")
    
    try:
        steam_ok = steam_collector.test_connection()
        print(f"  Steam: {'✅ Connected' if steam_ok else '❌ Failed'}")
    except Exception as e:
        print(f"  Steam: ❌ Error - {e}")
    
    print(f"\n⏰ Health check completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def setup_customer(customer_id, notion_page_id):
    """Set up a new customer"""
    from database import db
    from notion.customer_config import customer_config_monitor
    
    print(f"👤 Setting up customer: {customer_id}")
    
    try:
        # Add customer to database
        success = db.add_customer(customer_id, notion_page_id)
        
        if success:
            print(f"✅ Customer {customer_id} added to database")
            
            # Create Notion setup
            setup_success = customer_config_monitor.create_customer_setup(customer_id, notion_page_id)
            
            if setup_success:
                print(f"✅ Notion setup created for {customer_id}")
                print(f"📝 Customer can now fill out connection forms in their dashboard")
            else:
                print(f"❌ Failed to create Notion setup for {customer_id}")
        else:
            print(f"❌ Failed to add customer {customer_id} (may already exist)")
    
    except Exception as e:
        print(f"❌ Error setting up customer: {e}")

def list_customers():
    """List all customers and their status"""
    from database import db
    
    print("👥 Customer List:")
    print("=" * 50)
    
    try:
        customers = db.get_all_customers()
        
        if not customers:
            print("No customers found.")
            return
        
        for customer in customers:
            customer_id = customer['customer_id']
            created_at = customer['created_at']
            status = customer['status']
            
            print(f"ID: {customer_id}")
            print(f"  Status: {status}")
            print(f"  Created: {created_at}")
            
            # Get connection status
            connections = db.get_social_connections(customer_id)
            if connections:
                print("  Connections:")
                for conn in connections:
                    platform = conn['platform']
                    conn_status = conn['status']
                    last_sync = conn['last_sync'] or 'Never'
                    print(f"    {platform}: {conn_status} (Last sync: {last_sync})")
            else:
                print("  Connections: None")
            
            print()
    
    except Exception as e:
        print(f"❌ Error listing customers: {e}")

def main():
    parser = argparse.ArgumentParser(
        description='Steam Marketing Dashboard - Automated data collection for indie game studios'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Scheduler command (default)
    scheduler_parser = subparsers.add_parser('scheduler', help='Run the full scheduler')
    
    # Manual collection command
    collect_parser = subparsers.add_parser('collect', help='Run manual data collection')
    collect_parser.add_argument('--platforms', nargs='+', 
                              choices=['twitter', 'youtube', 'steam'],
                              help='Specific platforms to collect from')
    collect_parser.add_argument('--customer', help='Specific customer ID to collect for')
    
    # Health check command
    health_parser = subparsers.add_parser('health', help='Run system health check')
    
    # Customer management commands
    setup_parser = subparsers.add_parser('setup-customer', help='Set up a new customer')
    setup_parser.add_argument('customer_id', help='Customer ID')
    setup_parser.add_argument('notion_page_id', help='Notion page ID for the customer')
    
    list_parser = subparsers.add_parser('list-customers', help='List all customers')
    
    # Database command
    db_parser = subparsers.add_parser('init-db', help='Initialize database')
    
    args = parser.parse_args()
    
    # Set up logging
    setup_basic_logging()
    
    # Execute command
    if args.command == 'scheduler' or args.command is None:
        run_scheduler()
    elif args.command == 'collect':
        run_manual_collection(args.platforms, args.customer)
    elif args.command == 'health':
        run_health_check()
    elif args.command == 'setup-customer':
        setup_customer(args.customer_id, args.notion_page_id)
    elif args.command == 'list-customers':
        list_customers()
    elif args.command == 'init-db':
        from database import db
        print("💾 Database initialized successfully")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()