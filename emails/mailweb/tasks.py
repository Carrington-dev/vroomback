# feedback/tasks.py

from time import sleep
from django.core.mail import send_mail
# from celery import shared_task
from mailweb import settings
from mailweb.celery import app

@app.task
# @app.task(bind=True)
def send_feedback_email_task(email):
    """Sends an email when the feedback form has been submitted."""
    message = 'Hi there'
    # sleep(5)  
    send_mail(
        "Your Feedback",
        f"\t{message}\n\nThank you!",
        settings.DEFAULT_FROM_EMAIL,
        [email,],
        fail_silently=False,
    )

    return 'Email sent'

