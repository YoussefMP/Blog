import json
import os.path

from .models import Post, Tag
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from .utils.send_mail import send_me_mail
from django.http import HttpResponseBadRequest, JsonResponse
from django.core.validators import validate_email
from django.views.generic import DetailView, View
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt


class HomeView(View):

    tags = Tag.objects.all()
    posts = Post.objects.all().order_by('-date')
    context = {
        "posts": posts,
        "tags": tags,
    }

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, "OJ_Blog/Home.html", HomeView.context)

    def post(self, request):

        if request.method == 'POST' and 'sub-email' in request.POST:
            email = request.POST.get('sub-email')
            email = email.replace("<", "_l").replace(">", "_g")
            mode = "a" if os.path.exists("../emails.txt") else "w"
            with open("../emails.txt", mode, encoding="utf-8") as emails_file:
                emails_file.write(email)
                emails_file.write("\n")

            return JsonResponse({'success': 'Email subscribed successfully'})

        elif 'g-msg' in request.POST:
            # Handle the get in touch form
            name = request.POST.get('g-name')
            email = request.POST.get('g-email')
            message = request.POST.get('g-msg').replace("<", "_l").replace(">", "_g")

            send_me_mail(f"name: {name}\nemail: {email}\nmessage: {message}")

            return JsonResponse({'success': 'I will get back to you as soon as possible'})

    @staticmethod
    def check_email(email):
        try:
            validate_email(email)
        except ValidationError:
            return False
        return True


class BlogPostPage(DetailView):
    model = Post
    template_name = 'OJ_Blog/Post_Page.html'
    context_object_name = 'post'

    def get_object(self):
        title = self.kwargs.get('title')
        return get_object_or_404(Post, title=title)




