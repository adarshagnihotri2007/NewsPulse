import psycopg2


def connect_db():

    conn = psycopg2.connect(
        host="localhost",
        database="newspulse",
        user="postgres",
        password="Adarsh@2007",
        port="5432"
    )

    return conn

def insert_news(news, source):

    conn = connect_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO news (title, summary, link, published, source)
    VALUES (%s, %s, %s, %s, %s)
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
                source
            )
        )

    conn.commit()

    cursor.close()
    conn.close()