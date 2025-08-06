from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'bloghome/home.html')

def contact(request):
    return render(request, 'bloghome/contact.html')

def about(request):
    return render(request, 'bloghome/about.html')

