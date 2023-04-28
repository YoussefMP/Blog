from django.core.mail import get_connection
from django.core import mail
from django.conf import settings


def send_me_mail(body):
    email = mail.EmailMessage("New Message OJ_Blog", body,
                              settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER],
                              connection=get_connection())

    email.send()

