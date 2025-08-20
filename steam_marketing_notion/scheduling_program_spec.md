# Steam Marketing Dashboard - Scheduling & Data Update Program Specification

## Overview
A Python-based scheduling program that automatically collects marketing data from various APIs and updates a Notion dashboard for indie game studios. The program runs daily to gather social media, Steam, and marketing performance metrics.

---

## Core Components

### 1. Data Collection Engine
**Purpose**: Fetch data from multiple APIs and sources
**Components**:
- **Twitter/X API Client**: Collect followers, tweets, engagement metrics
- **YouTube API Client**: Collect subscribers, videos, performance data
- **Steam API Client**: Collect wishlist data and UTM campaign performance
- **Web Scraper**: Monitor press coverage and influencer content
- **Manual Data Handler**: Process manually inputted data (events, press)

### 2. Scheduler System
**Technology**: APScheduler (Advanced Python Scheduler)
**Schedule Types**:
- **Daily Collection** (runs at 2 AM): Social media and Steam data
- **Weekly Collection** (runs Sunday 3 AM): Influencer and press monitoring
- **Manual Triggers**: On-demand data refresh via API endpoint

### 3. Notion Integration Layer
**Purpose**: Format and upload data to Notion pages
**Components**:
- **Notion API Client**: Create/update pages, databases, blocks
- **Data Formatter**: Convert API responses to Notion-compatible format
- **Template Manager**: Handle Notion page layouts and structure

---

## Technical Architecture

### Data Flow
```
APIs/Sources → Data Collectors → Data Processors → Notion Formatters → Notion API → Dashboard
```

### Storage
- **SQLite Database**: Local cache for API responses and processing status
- **Configuration Files**: API keys, Notion page IDs, settings
- **Logs**: Detailed execution logs with error tracking

### Security
- Environment variables for API keys
- Rate limiting for all API calls
- Error handling and retry mechanisms
- Data validation before Notion upload

---

## Program Structure

### Main Modules

#### `scheduler.py`
- Main application entry point
- APScheduler configuration and job management
- Health check endpoints

#### `collectors/`
- `twitter_collector.py`: Twitter/X API integration
- `youtube_collector.py`: YouTube Data API integration  
- `steam_collector.py`: Steam Partner API integration
- `web_scraper.py`: Press and influencer content monitoring

#### `processors/`
- `data_processor.py`: Clean and normalize collected data
- `metrics_calculator.py`: Generate summary metrics and trends

#### `notion/`
- `notion_client.py`: Notion API wrapper
- `page_builder.py`: Create Notion page structures
- `database_updater.py`: Update Notion databases
- `customer_config.py`: Monitor customer setup forms and validate connections

#### `config/`
- `settings.py`: Configuration management
- `api_config.py`: API credentials and endpoints

---

## Daily Execution Workflow

### 2:00 AM - Main Data Collection
1. **Twitter Data Collection**
   - Fetch current follower count
   - Get tweets from past 24 hours with engagement metrics
   - Store in local database

2. **YouTube Data Collection**
   - Fetch current subscriber count
   - Get videos/shorts from past 24 hours with metrics
   - Store in local database

3. **Steam Data Collection**
   - Fetch current wishlist count and daily change
   - Collect UTM campaign performance data
   - Store in local database

4. **Data Processing**
   - Calculate daily summaries
   - Generate trend analysis
   - Prepare Notion-formatted data

5. **Notion Upload**
   - Update daily performance tables
   - Create new entries for posts/videos
   - Update summary dashboard

### Error Handling
- Retry failed API calls up to 3 times
- Log all errors with timestamps
- Send email alerts for critical failures
- Continue processing other sources if one fails

---

## Customer Onboarding & Interface (Notion-Based)

### Customer Setup Experience
All customer interactions happen within their Notion dashboard workspace:

#### 1. Account Setup Page Structure
```
📋 **Account Setup & Connections**
├── 🔗 Social Media Connections
│   ├── Twitter/X Setup Form
│   ├── YouTube Setup Form  
│   └── Connection Status Table
├── ⚙️ Dashboard Configuration
│   ├── Notification Preferences
│   └── Update Frequency Settings
└── 📊 Preview Dashboard
```

#### 2. Social Media Connection Forms

**Twitter/X Connection Database**
- Properties:
  - `API Key` (text)
  - `API Secret` (text, masked)
  - `Access Token` (text)
  - `Access Token Secret` (text, masked)
  - `Connection Status` (select: Pending/Connected/Failed/Testing)
  - `Last Sync` (date & time)
  - `Setup Date` (created date)

**YouTube Connection Database**
- Properties:
  - `Google Client ID` (text)
  - `Google Client Secret` (text, masked)
  - `Channel ID` (text)
  - `OAuth Status` (select: Pending/Authorized/Expired/Failed)
  - `Channel Name` (text, auto-populated)
  - `Last Sync` (date & time)

**Steam Integration Database**
- Properties:
  - `Steam Partner API Key` (text, masked)
  - `Game App ID` (number)
  - `Connection Status` (select: Pending/Connected/Failed)
  - `Last Sync` (date & time)

#### 3. Connection Status Dashboard
Real-time status table showing:
- ✅ **Twitter**: Connected (Last sync: 2 hours ago)
- ⏳ **YouTube**: Pending setup
- ❌ **Steam**: Invalid API key - Please check credentials
- 🔄 **System**: Next scheduled update in 6 hours

#### 4. Program Integration Workflow
```python
# notion/customer_config.py
def monitor_setup_databases():
    # Check for new connection entries every 5 minutes
    # Validate API credentials when new entries detected
    # Update connection status in real-time
    # Send test API calls to verify connectivity
    # Activate data collection once validated
```

### Customer Workflow
1. **Receive Notion template** with pre-built setup forms
2. **Fill connection forms** directly in their dashboard
3. **Real-time validation** - program tests credentials immediately
4. **Status updates** appear in Connection Status table
5. **Data collection begins** automatically once connected
6. **Dashboard populates** with their marketing data

---

## Notion Integration Specifications

### Page Structure
1. **Account Setup Page** (one-time configuration)
   - Connection forms and status tracking
   - Configuration preferences

2. **Main Dashboard Page**
   - Summary metrics callouts
   - Links to detailed sections

3. **Daily Performance Database**
   - Date, platform, metrics columns
   - Filterable and sortable

4. **Content Database** 
   - Individual posts/videos with engagement
   - Rich media embeds where possible

5. **Events & Press Database**
   - Manual entry forms
   - Status tracking

### Data Format
- **Metrics**: Numbers with trend indicators (↑↓)
- **Dates**: Standardized format (YYYY-MM-DD)
- **Links**: Rich link previews
- **Media**: Embedded thumbnails/previews

---

## Installation & Setup

### Requirements
```
notion-client==2.2.1
tweepy==4.14.0
google-api-python-client==2.108.0
apscheduler==3.10.4
requests==2.31.0
beautifulsoup4==4.12.2
python-dotenv==1.0.0
```

### Configuration Files
- `.env`: API keys and secrets
- `config.yaml`: Dashboard settings and page IDs
- `schedule_config.yaml`: Timing and frequency settings

### Environment Variables
```
TWITTER_API_KEY=
TWITTER_API_SECRET=
YOUTUBE_API_KEY=
STEAM_API_KEY=
NOTION_API_KEY=
NOTION_DATABASE_ID=
```

---

## Monitoring & Maintenance

### Logging
- Daily execution logs with status
- API response times and errors
- Data processing statistics

### Health Checks
- API connectivity tests
- Database integrity checks
- Notion upload success verification

### Backup Strategy
- Daily SQLite database backups
- Configuration file versioning
- Notion page templates backup

---

## Future Enhancements

### Phase 2 Features
- Real-time data updates via webhooks
- Custom alert thresholds
- Multi-game support for studios
- Advanced analytics and insights

### Scalability
- PostgreSQL database migration
- Docker containerization
- Cloud deployment options
- API rate limit optimization