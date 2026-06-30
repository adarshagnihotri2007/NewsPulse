import feedparser
from config import RSS_FEEDS
def fetch_news(source):
    url = RSS_FEEDS[source]
    feed = feedparser.parse(url)
    news_list = []

    for entry in feed.entries[:20]:
        
        article = {
            "title" : entry.get("title",""),
            "summary" : entry.get("summary",""),
            "link": entry.get("link", ""),
            "published": entry.get("published", "")
        }

        news_list.append(article)
    return news_list    
        