import feedparser
from config import RSS_FEEDS


def fetch_news(source, limit=20):

    news_list = []
    seen_links = set()

    # ---------- All Sources ----------
    if source == "all":

        urls = RSS_FEEDS.values()

    # ---------- Single Source ----------
    else:

        urls = [RSS_FEEDS[source]]

    # ---------- Fetch News ----------
    for url in urls:

        feed = feedparser.parse(url)

        entries = feed.entries

        if limit is not None:
            entries = entries[:limit]

        for entry in entries:

            link = entry.get("link", "")

            # Skip duplicate articles
            if link in seen_links:
                continue

            seen_links.add(link)

            article = {
                "title": entry.get("title", ""),
                "summary": entry.get("summary", ""),
                "link": link,
                "published": entry.get("published", "")
            }

            news_list.append(article)

    return news_list