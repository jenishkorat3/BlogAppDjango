from django.shortcuts import render, HttpResponse
from .models import Contact

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
