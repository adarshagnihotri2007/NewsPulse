import feedparser
def fetch_news():
    url = "https://feeds.bbci.co.uk/news/rss.xml"
    feed = feedparser.parse(url)
    news_list = []

    for entry in feed.entries[:5]:
        article = {
            "title" : entry.get("title",""),
            "summary" : entry.get("summary",""),
            "link": entry.get("link", ""),
            "published": entry.get("published", "")
        }

        news_list.append(article)
    return news_list    
        