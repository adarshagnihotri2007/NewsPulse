from config import RSS_FEEDS
from fetcher.news_fetcher import fetch_news

print("Available Sources")

for source_name in RSS_FEEDS:
    print(source_name)

source = input("Enter Source: ").lower()
keyword = input("Enter Keyword: ").lower()

if source in RSS_FEEDS:

    try:
        news = fetch_news(source)
        found = False

        for article in news:
          if keyword in article["title"].lower():
                found = True

                print("Title:", article["title"])
                print("Published:", article["published"])
                print("Link:", article["link"])
                print("-" * 80)
                
        if not found:
            print(f"No articles found for keyword: {keyword}")
            
    except Exception as e:
        print("Unable to fetch news!")
        print(f"Error: {e}")

else:
    print("Invalid Source!")