from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactFormSubmission

def home(request):
    return render(request, 'scoop_app/home.html')

def about(request):
    return render(request, 'scoop_app/about.html')

def products(request):
    return render(request, 'scoop_app/products.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            ContactFormSubmission.objects.create(
                name=name,
                email=email,
                message=message
            )
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('scoop_app:contact')
    
    return render(request, 'scoop_app/contact.html')
