import feedparser
from config import RSS_FEEDS


def fetch_news(source):

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

        for entry in feed.entries[:20]:

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