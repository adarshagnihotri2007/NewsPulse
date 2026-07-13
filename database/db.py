import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def connect_db():

    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    return conn


def insert_news(news, source):

    conn = connect_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO news (title, summary, link, published, source, sentiment)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON CONFLICT (link) DO NOTHING;
    """

    for article in news:

        cursor.execute(
            query,
            (
                article.get("title", ""),
                article.get("summary", ""),
                article.get("link", ""),
                article.get("published", ""),
                source,
                article.get("sentiment", "")
            )
        )

    conn.commit()

    cursor.close()
    conn.close()