from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def education(request):
    return render(request, 'education.html', {})

def competences(request):
    return render(request, 'competences.html', {})

def projets(request):
    return render(request, 'projets.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def submit_mail(request):
    if request.method == "POST":
        message = request.POST["message"]
        email = request.POST["email"]
        message_subject = request.POST["sujet"]
        print(email)
        send_mail(
            message_subject,
            message,
            email,
            ['sengmanynicolas21@gmail.com'],
            fail_silently=False,
        )
        messages.success(request, "Message bien envoyé ! ")

    return render(request, 'contact.html')