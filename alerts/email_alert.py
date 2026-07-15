import os
import csv
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def create_csv(results, source, keyword):

    filename = f"{source}_{keyword}_results.csv"

    filepath = os.path.join("temp", filename)

    with open(filepath, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "title",
                "summary",
                "published",
                "source",
                "sentiment",
                "link"
            ]
        )

        writer.writeheader()

        for article in results:

            writer.writerow(
                {
                    "title": article.get("title", ""),
                    "summary": article.get("summary", ""),
                    "published": article.get("published", ""),
                    "source": article.get("source", ""),
                    "sentiment": article.get("sentiment", ""),
                    "link": article.get("link", "")
                }
            )

    return filepath


def send_search_results(
    receiver_email,
    source,
    keyword,
    results,
    csv_path
):

    sender_email = os.getenv("EMAIL")
    app_password = os.getenv("APP_PASSWORD")
    

    msg = EmailMessage()

    msg["Subject"] = f"NewsPulse Search Results - {keyword.title()}"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    body = f"""Hello,

Your NewsPulse search has been completed successfully.

Source : {source.upper()}
Keyword : {keyword}
Total Results : {len(results)}

============================================================
"""
    if len(results) > 10:

        body += """   
Showing Top 5 Results.
Complete report is attached as a CSV file.

============================================================
"""

    if len(results) == 0:

        body += "\nNo matching news articles were found.\n"

    else:
        articles_to_send = results

        if len(results) > 10:
            articles_to_send = results[:5]

        for index, article in enumerate(articles_to_send, start=1):

            body += f"""
Result {index}

Title      : {article.get("title", "")}

Published  : {article.get("published", "N/A")}

Source     : {article.get("source", "N/A")}

Sentiment  : {article.get("sentiment", "N/A")}

Summary    : {article.get("summary", "")}

Link       : {article.get("link", "")}

------------------------------------------------------------
"""

    body += """

Thank you for using NewsPulse.

Regards,
NewsPulse
"""

    msg.set_content(body)
    if csv_path:
      with open(csv_path, "rb") as file:
          
          msg.add_attachment(
              file.read(),
              maintype="application",
              subtype="octet-stream",
              filename=os.path.basename(csv_path)
          )    


    try:

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(sender_email, app_password)

        server.send_message(msg)

        server.quit()

        print("✅ Search results emailed successfully!")

    except Exception as e:

        print("❌ Failed to send email.")
        print(e)

    finally:

        if csv_path and os.path.exists(csv_path):

            os.remove(csv_path)