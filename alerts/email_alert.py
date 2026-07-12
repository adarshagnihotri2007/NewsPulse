import smtplib
from email.message import EmailMessage


def send_search_results():

    sender_email = "adarshagnihotri2004@gmail.com"
    receiver_email = "adarshagnihotri2004@gmail.com"

    app_password = "YOUR_APP_PASSWORD"

    msg = EmailMessage()

    msg["Subject"] = "NewsPulse Test Email"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.set_content(
        """Hello!

This is a test email sent from NewsPulse.

If you received this email, SMTP configuration is working successfully.

Regards,
NewsPulse
"""
    )

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(sender_email, app_password)

    server.send_message(msg)

    server.quit()

    print("✅ Email sent successfully!")


# send_search_results()

