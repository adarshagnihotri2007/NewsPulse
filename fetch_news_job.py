import socket
import time

from fetcher.news_fetcher import fetch_news
from sentiment.sentiment import analyze_sentiment
from database.db import insert_news

def is_internet_available():

    try:

        socket.create_connection(("8.8.8.8", 53), timeout=5)

        return True

    except OSError:

        return False


def fetch_all_news():

    max_retries = 10

    for attempt in range(max_retries):

        if is_internet_available():

            print("🌐 Internet Connected.")

            break

        print(f"❌ No Internet. Retrying in 10 seconds... ({attempt + 1}/{max_retries})")

        time.sleep(10)
        
    else:

        print("❌ Internet not available after multiple attempts.")

        return

    print("Fetching latest news...")

    news = fetch_news("all", limit=None)

    print(f"Total Articles Fetched: {len(news)}")

    for article in news:

        sentiment = analyze_sentiment(
            article.get("title", ""),
            article.get("summary", "")
        )

        article["sentiment"] = sentiment

    insert_news(news, "all")

    print("News saved successfully to PostgreSQL.")


if __name__ == "__main__":

    fetch_all_news()