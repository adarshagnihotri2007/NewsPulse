import csv

from config import RSS_FEEDS
from fetcher.news_fetcher import fetch_news
from database.db import insert_news
from sentiment.sentiment import analyze_sentiment
from alerts.email_alert import send_search_results, create_csv


print("Available Sources")

for source_name in RSS_FEEDS:
    print(source_name)

print("all")

source = input("\nEnter Source: ").strip().lower()
keyword = input("Enter Keyword: ").strip().lower()


if source in RSS_FEEDS or source == "all":

    try:

        news = fetch_news(source)
        print(f"\nTotal Articles Fetched: {len(news)}")

        # ---------- Sentiment Analysis ----------
        for article in news:

            sentiment = analyze_sentiment(
                article.get("title", ""),
                article.get("summary", "")
            )

            article["sentiment"] = sentiment

        # ---------- Save to PostgreSQL ----------
        insert_news(news, source)

        # ---------- Save to CSV ----------
        with open("news.csv", "w", newline="", encoding="utf-8") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "title",
                    "summary",
                    "link",
                    "published",
                    "source",
                    "sentiment"
                ]
            )

            writer.writeheader()

            for article in news:
                writer.writerow(article)

        # ---------- Keyword Search ----------
        found = False

        matched_articles = []

        for article in news:

            title = article.get("title", "")
            summary = article.get("summary", "")

            if (
                keyword in title.lower()
                or keyword in summary.lower()
            ):

                found = True

                matched_articles.append(article)

                print(f"\nTitle      : {title}")
                print(f"Published  : {article.get('published', 'N/A')}")
                print(f"Source     : {article.get('source', 'N/A')}")
                print(f"Link       : {article.get('link', 'N/A')}")
                print(f"Summary    : {summary}")
                print(f"Sentiment  : {article.get('sentiment')}")
                print("-" * 100)

        if not found:

            print(f"\nNo articles found for keyword: {keyword}")

        else:

            choice = input(
                "\n📧 Send these results to your email? (yes/no): "
            ).strip().lower()

            if choice == "yes":

                receiver_email = input(
                    "Enter your email: "
                ).strip()

                csv_path = None

                if len(matched_articles) > 10:

                    csv_path = create_csv(
                        matched_articles,
                        source,
                        keyword
                    )
                

                send_search_results(
                    receiver_email,
                    source,
                    keyword,
                    matched_articles,
                    csv_path
                )

        print("\nNews successfully saved to PostgreSQL and news.csv")

    except Exception as e:

        print("Unable to fetch news!")
        print(f"Error: {e}")

else:

    print("Invalid Source!")