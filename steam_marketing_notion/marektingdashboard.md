# Indie Game Marketing Dashboard Specification

## Overview
This dashboard is for indie game studio customers to monitor the performance of marketing campaigns and related activities.  
The dashboard will be hosted and accessible via **Notion** and should pull data automatically from connected accounts and external sources.

---

## 1. Social Account Integration
- Allow customers to connect:
  - **Twitter (X) account**
  - **YouTube channel**
- Enable:
  - Posting and scheduling tweets/videos
  - Managing and editing social media content
- Authentication via official APIs (Twitter API, YouTube Data API)

---

## 2. Twitter Performance (Daily)
- Data to collect (per day):
  - **Total followers** (current count)
  - **Number of tweets posted that day**
  - For each tweet:
    - Views
    - Likes
    - Retweets
    - Comments (replies)
- Display format:
  - Table view: date-wise performance summary
  - Individual tweet cards with engagement metrics

---

## 3. YouTube Performance (Daily)
- Data to collect (per day):
  - **Total subscribers** (current count)
  - **Number of videos/shorts posted that day**
  - For each video/short:
    - Views
    - Likes
    - Comments
- Display format:
  - Table view: date-wise performance summary
  - Individual video cards with engagement metrics and thumbnails

---

## 4. Steam Performance (Daily)
- Data to collect:
  - **Daily wishlists** (total and net change)
  - UTM campaign performance:
    - Source (e.g., Twitter, YouTube, press, influencer)
    - Clicks and conversions to wishlist
- Display format:
  - Line chart for wishlist growth over time
  - Table for UTM analysis with sorting by conversions

---

## 5. Influencer Content Tracker
- Track YouTube/Twitch/Twitter/other influencer content mentioning the game
- Data to collect:
  - Influencer name & platform
  - Link to content
  - Date posted
  - View count, likes, comments (if available)
- Display format:
  - List with filters by date/platform
  - Embedded previews if possible

---

## 6. Press Coverage Tracker
- Track articles mentioning the game
- Data to collect:
  - Publication name
  - Link to article
  - Date published
  - Short summary or headline
- Display format:
  - List with filters by date/publication
  - Embedded link previews

---

## 7. Upcoming Online Events
- Track relevant online events and application status for the customer’s game
- Data to collect:
  - Event name
  - Date(s)
  - Application deadline
  - Application status (Not Applied / Applied / Accepted / Rejected)
  - Link to event page
- Display format:
  - Calendar view for upcoming events
  - Table view for application status

---

## 8. General Requirements
- Dashboard should be **readable inside Notion**
- Data should **auto-update daily** where possible
- Manual input allowed for influencer/press/events if automation is not possible
- Simple, visually clear charts and tables
- Filters for date range, platform, and campaign

---

## API & Data Sources
- **Twitter/X API**
- **YouTube Data API**
- **Steam Partner API** (for wishlist data)
- **Google Analytics** or equivalent (for UTM tracking)
- Web scraping/RSS feeds (for press articles if no API)
- Manual admin input for unautomated data

---

## Example Layout (Notion Page)
1. **Top Summary Section**
   - Key metrics (followers, subscribers, daily wishlists, top-performing post)
2. **Social Media Performance**
   - Twitter section
   - YouTube section
3. **Steam Performance**
4. **Influencer Coverage**
5. **Press Coverage**
6. **Upcoming Events**
