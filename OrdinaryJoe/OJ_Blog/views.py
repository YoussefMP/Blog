from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import DetailView


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




