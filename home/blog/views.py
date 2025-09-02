from django.shortcuts import render, redirect
from .models import BlogComment, Post
from django.contrib import messages

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post).order_by('-timestamp')
    return render(request, 'blog/post.html', {'post': post, 'comments': comments, 'user': request.user})

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.filter(sno=postSno).first()
        if post:
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
    return redirect("blogPost", slug=post.slug)
