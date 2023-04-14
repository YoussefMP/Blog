from django.shortcuts import render, get_object_or_404
from email.mime.application import MIMEApplication
from django.views.generic.edit import FormView
from email.mime.multipart import MIMEMultipart
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.core.mail import get_connection
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.files import File
from django.conf import settings
from .forms import ContactForm
from django.core import mail
from .models import Post
import io


def home(request):

    posts = Post.objects.all().order_by('-date')
    context = {
        "posts": posts,
        "numbers": [i for i in range(10)],
    }

    return render(request, "OJ_Blog/Home.html", context)


class BlogPostPage(DetailView):
    model = Post
    template_name = 'OJ_Blog/Post_Page.html'
    context_object_name = 'post'

    def get_object(self):
        title = self.kwargs.get('title')
        return get_object_or_404(Post, title=title)


class ContactView(TemplateView):
    template_name = 'OJ_Blog/contact.html'

    def post(self, request, *args, **kwargs):

        print(f"REQUEST {request}")

        # get form data from POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('remarks')
        agree = request.POST.get('agree', False)
        document = request.FILES.get('document')

        # validate form data
        if not all([name, email, agree]):
            error_message = 'Please fill out all required fields.'
            return self.render_to_response({'error_message': error_message})

        # send email with form data
        subject = 'New Contact Form Submission'
        message = f'''
            Name: {name}
            Email: {email}
            Message: {message}
        '''

        email_from = settings.EMAIL_HOST_USER
        email_to = [settings.EMAIL_HOST_USER, email]
        if document:

            message += 'Document: See attached\n'
            attachment = MIMEApplication(document.read(), _subtype=document.content_type.split('/')[-1])
            attachment.add_header('Content-Disposition', 'attachment', filename=document.name)
            email_attachments = [attachment]

        else:
            email_attachments = None

        # send_mail(subject, message, email_from, email_to, fail_silently=False, attachments=email_attachments)

        # connection = mail.get_connection('django.core.mail.backends.console.EmailBackend')
        print(message)
        email = mail.EmailMessage(subject, message,
                                  email_from, email_to,
                                  connection=get_connection())

        if email_attachments:
            for attachment in email_attachments:
                email.attach(attachment)
        email.send()

        # return success message
        success_message = 'Your message has been sent. We will be in touch soon!'
        return self.render_to_response({'success_message': success_message})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['languages'] = ['English', 'Spanish', 'French', 'German', 'Italian']
        return context

