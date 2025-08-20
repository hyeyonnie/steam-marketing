# Steam Marketing Dashboard - Automated Data Collection & Notion Integration

A comprehensive Python-based system that automatically collects marketing data from Twitter/X, YouTube, and Steam APIs, then updates Notion dashboards for indie game studios.

## Features

- **Multi-Platform Data Collection**: Twitter/X, YouTube, Steam
- **Automated Scheduling**: Daily and weekly data collection
- **Notion Integration**: Real-time dashboard updates
- **Customer Management**: Self-service setup via Notion forms
- **Press Monitoring**: Web scraping for mentions and coverage
- **Performance Analytics**: Engagement metrics and growth tracking
- **Anomaly Detection**: Automatic alerts for significant changes

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd steam-marketing-dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API credentials
   ```

4. **Configure settings**
   ```bash
   # Edit config.yaml for scheduling and rate limits
   ```

## Configuration

### Environment Variables (.env)

```bash
# Twitter/X API Credentials
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret

# YouTube API Credentials
YOUTUBE_API_KEY=your_youtube_api_key

# Steam API Credentials
STEAM_API_KEY=your_steam_api_key

# Notion API Credentials
NOTION_API_KEY=your_notion_integration_token
NOTION_DATABASE_ID=your_notion_database_id
```

### Required API Keys

1. **Twitter/X API**: Apply at [developer.twitter.com](https://developer.twitter.com)
2. **YouTube Data API**: Create project at [Google Cloud Console](https://console.cloud.google.com)
3. **Steam Web API**: Register at [steamcommunity.com/dev/apikey](https://steamcommunity.com/dev/apikey)
4. **Notion API**: Create integration at [notion.so/my-integrations](https://www.notion.so/my-integrations)

## Usage

### Starting the Scheduler

```bash
python scheduler.py
```

The scheduler will automatically:
- Collect data daily at 2:00 AM
- Run weekly press monitoring on Sundays at 3:00 AM
- Monitor customer configurations every 5 minutes
- Perform health checks hourly

### Manual Data Collection

```bash
# Collect data for all customers
python -c "from scheduler import MarketingScheduler; s = MarketingScheduler(); s.daily_data_collection()"

# Run press monitoring
python -c "from scheduler import MarketingScheduler; s = MarketingScheduler(); s.weekly_data_collection()"
```

### Database Management

```bash
# Initialize database
python -c "from database import db; print('Database initialized')"

# Add a customer
python -c "from database import db; db.add_customer('customer123', 'notion_page_id')"
```

## Customer Onboarding

1. **Share Notion Template**: Provide customers with the pre-built Notion template
2. **Customer Setup**: Customers fill out connection forms in their dashboard
3. **Automatic Validation**: System validates API credentials in real-time
4. **Data Collection**: Begins automatically once connections are validated
5. **Dashboard Population**: Marketing data appears in their Notion dashboard

### Notion Template Structure

```
📋 Marketing Dashboard
├── 🔗 Account Setup & Connections
│   ├── Twitter/X Connection Form
│   ├── YouTube Connection Form
│   └── Steam Connection Form
├── 📊 Daily Performance Database
├── 📱 Content Database
└── 📰 Events & Press Database
```

## Architecture

### Data Flow
```
APIs/Sources → Data Collectors → Data Processors → Notion Formatters → Notion API → Dashboard
```

### Core Components

1. **Data Collectors** (`collectors/`)
   - `twitter_collector.py`: Twitter/X API integration
   - `youtube_collector.py`: YouTube Data API integration
   - `steam_collector.py`: Steam Web API integration
   - `web_scraper.py`: Press and influencer monitoring

2. **Data Processors** (`processors/`)
   - `data_processor.py`: Clean and normalize data
   - `metrics_calculator.py`: Generate analytics and summaries

3. **Notion Integration** (`notion/`)
   - `notion_client.py`: Notion API wrapper
   - `page_builder.py`: Create Notion structures
   - `customer_config.py`: Monitor setup forms

4. **Configuration** (`config/`)
   - `settings.py`: Configuration management
   - `api_config.py`: API credentials and endpoints

## Monitoring & Maintenance

### Logs
- Application logs: `./logs/marketing_scheduler.log`
- Error tracking with detailed timestamps
- Performance metrics and API response times

### Health Checks
- Automatic API connectivity tests
- Database integrity validation
- Processing status monitoring

### Data Retention
- Daily performance: 90 days (configurable)
- Content data: 30 days
- Processing logs: 30 days

## API Rate Limits

- **Twitter**: 75 requests/minute
- **YouTube**: 10,000 requests/day
- **Steam**: 100 requests/minute
- **Notion**: 3 requests/second

## Error Handling

- Automatic retry with exponential backoff
- Graceful degradation if one API fails
- Email alerts for critical failures
- Continuation of processing for available platforms

## Security

- Environment variables for sensitive credentials
- No credentials stored in code or logs
- Rate limiting to respect API terms
- Data validation before storage

## Deployment Options

### Local Development
```bash
python scheduler.py
```

### Production (systemd service)
```bash
# Create service file: /etc/systemd/system/marketing-scheduler.service
sudo systemctl enable marketing-scheduler
sudo systemctl start marketing-scheduler
```

### Docker (Future Enhancement)
```bash
docker build -t marketing-scheduler .
docker run -d --env-file .env marketing-scheduler
```

## Troubleshooting

### Common Issues

1. **API Authentication Failures**
   - Verify credentials in `.env` file
   - Check API key permissions and quotas
   - Review API documentation for changes

2. **Database Connection Issues**
   - Ensure SQLite file permissions
   - Check disk space availability
   - Verify database path in configuration

3. **Notion Integration Problems**
   - Confirm integration has proper permissions
   - Verify page/database IDs are correct
   - Check Notion API rate limits

### Debug Mode
```bash
# Enable debug logging
export LOG_LEVEL=DEBUG
python scheduler.py
```

## Support

For technical support or feature requests:
1. Check the troubleshooting guide above
2. Review application logs for error details
3. Verify API credentials and rate limits
4. Contact support with specific error messages

## License

This project is proprietary software for marketing service clients.

---

**Version**: 1.0.0  
**Last Updated**: 2025-01-15