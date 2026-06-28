from config import RSS_FEEDS
from fetcher.news_fetcher import fetch_news

print("Available Sources")

for source_name in RSS_FEEDS:
    print(source_name)

source = input("Enter Source: ").lower()

if source in RSS_FEEDS:

    try:
        news = fetch_news(source)

        for article in news:
            print("Title:", article["title"])
            print("Published:", article["published"])
            print("Link:", article["link"])
            print("-" * 80)

    except Exception as e:
        print("Unable to fetch news!")
        print(f"Error: {e}")

else:
    print("Invalid Source!")