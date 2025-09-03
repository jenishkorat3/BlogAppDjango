from django.shortcuts import render, redirect
from .models import BlogComment, Post
from django.contrib import messages
from blog.templatetags import extras

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post, parent=None).order_by('-timestamp')
    replies = BlogComment.objects.filter(post=post).exclude(parent=None).order_by('-timestamp')
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict:
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    return render(request, 'blog/post.html', {'post': post, 'comments': comments, 'user': request.user, 'replyDict': replyDict})

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.filter(sno=postSno).first()
        parentSno = request.POST.get('parentSno')

        if post and parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent = BlogComment.objects.filter(sno=parentSno).first()
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")

    return redirect("blogPost", slug=post.slug)
