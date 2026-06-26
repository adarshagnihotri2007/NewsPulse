from fetcher.news_fetcher import fetch_news

news = fetch_news()

for article in news:

    print("Title      :", article["title"])
    print("Published  :", article["published"])
    print("Link       :", article["link"])
    print("-" * 80)