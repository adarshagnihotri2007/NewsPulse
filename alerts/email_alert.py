import smtplib
from email.message import EmailMessage


def send_search_results(
    receiver_email,
    source,
    keyword,
    results
):

    sender_email = "YOUR_EMAIL@gmail.com"
    app_password = "YOUR_APP_PASSWORD"

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

    if len(results) == 0:

        body += "\nNo matching news articles were found.\n"

    else:

        for index, article in enumerate(results, start=1):

            body += f"""
Result {index}

Title      : {article.get("title", "")}

Published  : {article.get("published", "N/A")}

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