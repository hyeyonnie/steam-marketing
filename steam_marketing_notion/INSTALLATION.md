# Installation Guide - Steam Marketing Dashboard

## Prerequisites

- Python 3.8 or higher
- Internet connection for API access
- API credentials for Twitter/X, YouTube, Steam, and Notion

## Quick Start

### 1. Environment Setup

```bash
# Create virtual environment (recommended)
python -m venv marketing_env
source marketing_env/bin/activate  # On Windows: marketing_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit configuration files
# .env - Add your API credentials
# config.yaml - Adjust scheduling and settings
```

### 3. API Credentials Setup

#### Twitter/X API
1. Visit [developer.twitter.com](https://developer.twitter.com)
2. Create a new app
3. Generate API keys and access tokens
4. Add to `.env`:
   ```
   TWITTER_API_KEY=your_api_key
   TWITTER_API_SECRET=your_api_secret
   TWITTER_ACCESS_TOKEN=your_access_token
   TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
   ```

#### YouTube Data API
1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project or select existing
3. Enable YouTube Data API v3
4. Create API key
5. Add to `.env`:
   ```
   YOUTUBE_API_KEY=your_youtube_api_key
   ```

#### Steam Web API
1. Visit [steamcommunity.com/dev/apikey](https://steamcommunity.com/dev/apikey)
2. Register for a Steam Web API key
3. Add to `.env`:
   ```
   STEAM_API_KEY=your_steam_api_key
   ```

#### Notion API
1. Go to [notion.so/my-integrations](https://www.notion.so/my-integrations)
2. Create a new integration
3. Copy the Internal Integration Token
4. Add to `.env`:
   ```
   NOTION_API_KEY=your_notion_integration_token
   NOTION_DATABASE_ID=your_main_database_id
   ```

### 4. Database Initialization

```bash
# Initialize the SQLite database
python run.py init-db
```

### 5. Test Installation

```bash
# Run health check
python run.py health

# Expected output:
# 📋 Configuration:
#   twitter: ✅ Valid
#   youtube: ✅ Valid
#   steam: ✅ Valid
#   notion: ✅ Valid
# 💾 Database:
#   Connection: ✅ Active
#   Customers: 0
# 🌐 API Connections:
#   Twitter: ✅ Connected
#   YouTube: ✅ Connected
#   Steam: ✅ Connected
```

## Detailed Configuration

### Environment Variables (.env)

```bash
# Required API Keys
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret

YOUTUBE_API_KEY=your_youtube_api_key
GOOGLE_CLIENT_ID=your_google_client_id  # Optional for OAuth
GOOGLE_CLIENT_SECRET=your_google_client_secret  # Optional for OAuth

STEAM_API_KEY=your_steam_api_key

NOTION_API_KEY=your_notion_integration_token
NOTION_DATABASE_ID=your_notion_database_id

# Optional Settings
DATABASE_PATH=./data/marketing_data.db
LOG_LEVEL=INFO
LOG_FILE=./logs/marketing_scheduler.log

# Email Alerts (Optional)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
ALERT_EMAIL=alerts@yourdomain.com
```

### Scheduling Configuration (config.yaml)

```yaml
# Modify these settings as needed
schedule:
  daily_collection_time: "02:00"  # 2:00 AM
  weekly_collection_day: "sunday"
  weekly_collection_time: "03:00"  # 3:00 AM Sunday
  customer_config_check_interval: 300  # 5 minutes

# API Rate Limits (adjust based on your API plans)
rate_limits:
  twitter: 75      # requests per minute
  youtube: 10000   # requests per day
  steam: 100       # requests per minute
  notion: 3        # requests per second
```

## Running the System

### Development Mode
```bash
# Run scheduler (blocks terminal)
python run.py scheduler

# Run in background (Linux/Mac)
nohup python run.py scheduler > scheduler.log 2>&1 &

# Run in background (Windows)
start /B python run.py scheduler
```

### Production Deployment

#### Using systemd (Linux)

1. Create service file:
```bash
sudo nano /etc/systemd/system/marketing-scheduler.service
```

2. Add service configuration:
```ini
[Unit]
Description=Steam Marketing Dashboard Scheduler
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/steam-marketing-dashboard
Environment=PATH=/path/to/marketing_env/bin
ExecStart=/path/to/marketing_env/bin/python run.py scheduler
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

3. Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable marketing-scheduler
sudo systemctl start marketing-scheduler

# Check status
sudo systemctl status marketing-scheduler
```

#### Using Windows Service

1. Install pywin32:
```bash
pip install pywin32
```

2. Create service wrapper (advanced setup required)

#### Using Task Scheduler (Windows)

1. Open Task Scheduler
2. Create Basic Task
3. Set trigger for system startup
4. Set action to start your Python script
5. Configure to run whether user is logged on or not

## Customer Onboarding Setup

### 1. Create Notion Template

1. Create a new Notion page for the customer
2. Share the page with your Notion integration
3. The system will automatically create:
   - Connection setup databases
   - Performance tracking databases
   - Dashboard pages

### 2. Add Customer to System

```bash
# Add new customer
python run.py setup-customer "customer123" "notion_page_id_here"

# List all customers
python run.py list-customers
```

### 3. Customer Instructions

Send customers:
1. Link to their Notion dashboard
2. Instructions to fill out connection forms
3. API credential requirements for their platforms

## Troubleshooting

### Common Issues

#### "Module not found" errors
```bash
# Ensure virtual environment is activated
source marketing_env/bin/activate  # Linux/Mac
marketing_env\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

#### Database permission errors
```bash
# Check file permissions
ls -la data/
chmod 664 data/marketing_data.db

# Create data directory if missing
mkdir -p data logs
```

#### API authentication failures
```bash
# Test individual APIs
python -c "from collectors.twitter_collector import twitter_collector; print(twitter_collector.test_connection())"
python -c "from collectors.youtube_collector import youtube_collector; print(youtube_collector.test_connection())"
python -c "from collectors.steam_collector import steam_collector; print(steam_collector.test_connection())"
```

#### Notion integration issues
1. Verify integration has access to target pages
2. Check integration capabilities (read content, update content, insert content)
3. Ensure page/database IDs are correct

### Debug Mode

```bash
# Enable detailed logging
export LOG_LEVEL=DEBUG
python run.py health

# Check logs
tail -f logs/marketing_scheduler.log
```

### Getting Help

1. Check the main README.md for usage instructions
2. Review log files for specific error messages
3. Verify all API credentials are correct and active
4. Test with a single customer before scaling up

## Security Considerations

- Keep `.env` file secure and never commit to version control
- Use environment-specific API keys (dev/prod)
- Regularly rotate API credentials
- Monitor API usage and rate limits
- Set up log rotation to prevent disk space issues

## Performance Optimization

- Adjust rate limits based on your API plans
- Consider running different collections at different times
- Monitor memory usage with multiple customers
- Use database cleanup regularly to maintain performance

---

Need help? Check the troubleshooting section or contact technical support.