import feedparser
from email.utils import parsedate_to_datetime
from config import RSS_FEEDS


def fetch_news(source, limit=20):

    news_list = []
    seen_links = set()

    # ---------- All Sources ----------
    if source == "all":

        sources = RSS_FEEDS.items()

    # ---------- Single Source ----------
    else:

        sources = [(source,RSS_FEEDS[source])]

    # ---------- Fetch News ----------
    for source_name, url in sources:

        feed = feedparser.parse(url)

        entries = feed.entries

        if limit is not None:
            entries = entries[:limit]

        for entry in entries:

            link = entry.get("link", "")

            published = entry.get("published", "")

            try:
                published = parsedate_to_datetime(published).isoformat()

            except Exception:  
                pass  

            # Skip duplicate articles
            if link in seen_links:
                continue
    

            # Skip duplicate articles
            if link in seen_links:
                continue

            seen_links.add(link)

            article = {
                "title": entry.get("title", ""),
                "summary": entry.get("summary", ""),
                "link": link,
                "published": published,
                "source": source_name
            }

            news_list.append(article)

    return news_list