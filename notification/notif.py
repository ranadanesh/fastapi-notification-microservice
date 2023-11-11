import yagmail
from notification.core import EMAIL_PASSWORD


def send_notif(email, content):
    try:

        yag = yagmail.SMTP(user='ranadanesh.79@gmail.com', password=EMAIL_PASSWORD)
        yag.send(to=email, subject='Testing Notification', contents=content)
        print("Email sent successfully")
    except Exception as e:
        print("Error, email was not sent")
        print(e)

