# 📰 NewsPulse

An automated **News Sentiment Analysis System** built using **Python, PostgreSQL, Power BI, and TextBlob**. The project fetches news from multiple RSS feeds, analyzes article sentiment, stores the data in PostgreSQL, sends email alerts, and visualizes insights through an interactive Power BI dashboard.

---

## 📊 Dashboard

![NewsPulse Dashboard](assets/dashboard.png)

---

## ✨ Features

- 📰 Fetch news from multiple RSS feeds
- 😊 Perform sentiment analysis using TextBlob
- 🗄️ Store news articles in PostgreSQL
- 🔍 Search news by keyword
- 📧 Send email alerts with matching articles
- 📊 Interactive Power BI dashboard
- 📈 Analyze sentiment distribution
- 🌍 Compare news sources
- 📋 View the latest news articles

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | News Fetching & Processing |
| PostgreSQL | Database |
| Power BI | Dashboard & Visualization |
| TextBlob | Sentiment Analysis |
| Feedparser | RSS Feed Parsing |
| Git & GitHub | Version Control |

---

## 📈 Dashboard Highlights

- 📄 Total Articles
- 😊 Positive Articles
- 😐 Neutral Articles
- ☹️ Negative Articles
- 📊 Articles by Source
- 🍩 Sentiment Distribution
- 📊 Sentiment by Source
- 📰 Latest Articles

---

## ⚙️ Project Workflow

```text
RSS Feeds
     │
     ▼
News Fetcher (Python)
     │
     ▼
Sentiment Analysis (TextBlob)
     │
     ▼
PostgreSQL Database
     │
     ├────────► Email Alerts
     │
     ▼
Power BI Dashboard
```

---

## 📂 Project Structure

```text
News_Pulse
│
├── alerts/
├── assets/
├── database/
├── fetcher/
├── Powerbi/
├── sentiment/
├── temp/
├── config.py
├── fetch_news_job.py
├── main.py
├── README.md
└── requirements.txt
```

---

## ▶️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/adarshagnihotri2007/News_Pulse.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the project

```bash
python main.py
```

---

## 👨‍💻 Author

**Adarsh Agnihotri**

**B.Tech – Artificial Intelligence & Data Science**