from django.shortcuts import render, HttpResponse
from .models import Contact
from blog.models import Post

# Create your views here.
def home(request):
    return render(request, 'bloghome/home.html')

def contact(request):
    isSubmitted = False
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        isSubmitted = True
    return render(request, 'bloghome/contact.html', {'isSubmitted': isSubmitted})

def about(request):
    return render(request, 'bloghome/about.html')

def search(request):
    query = request.GET.get('query')
    if len(query) > 78:
        posts = Post.objects.none()
    else:
        posts = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)

    return render(request, 'bloghome/search.html', {'query' : query ,'posts': posts})
