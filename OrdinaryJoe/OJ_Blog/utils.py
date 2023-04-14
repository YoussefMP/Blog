from django.core.mail import send_mail


def send_welcome_email(email):
    send_mail(
       'Welcome to my blog!',
       'Thank you for signing up!',
       'from@example.com',
       [email],
       fail_silently=False,
    )
