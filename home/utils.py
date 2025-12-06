
"""import smtp
from email.mime.text import MIMEText
from django.conf import settings
"""
from home.models impport MenuItem
"""
def send_custom_email(recipient_email, subject, message_body) :
    try :
        msg = MIMEText(message_body)
        msg["Subject"] = subject
        msg["From"] = settings.EMAIL_HOST_USER
        msg["To"] = recipient_email

        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server :
            server.starttls()
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD) 
            server.sendmail(settings.EMAIL_HOST_USER, [recipient_email], msg.as_string())

        return True

    except smtplib.SMTPRecipientsRefused :
        return "Invalid Recipient email address"
    except Exception as e :
        return f"Email sending failed : {str(e)}"
"""

def get_distinct_cuisines() :
    cuisine_names = (
        MenuItem.objects.values_list("cuisine_name", flat = True)
        .distinct()
        .order_by("cuisine_name")
    )
    return list(cuisine_name)