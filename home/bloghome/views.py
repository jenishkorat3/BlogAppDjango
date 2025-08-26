from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib import messages

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

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')

        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')

        user = User.objects.create_user(username, email, pass1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(request, "Your iCoder account has been sucessfully created.")

        return redirect('home')
    else:
        return HttpResponse('404 - Not Allowed')
