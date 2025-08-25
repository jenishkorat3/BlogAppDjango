from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    return render(request, 'blog/post.html', {'post': post})
