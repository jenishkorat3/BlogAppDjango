from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def blogPost(request, slug):
    return render(request, 'blog/post.html', {'slug': slug})
