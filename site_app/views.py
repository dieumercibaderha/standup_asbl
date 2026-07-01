from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Inscription

from django.core.mail import send_mail
from .models import Inscription
from site_project.settings import *

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .models import Inscription

def send_newsletter(subject, message):
    subscribers = Inscription.objects.all()
    recipient_list = [s.email for s in subscribers]
    
    send_mail(
        subject,
        message,
        'ton_email@gmail.com',
        recipient_list,
        fail_silently=False,
    )



def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not Inscription.objects.filter(email=email).exists():  # Vérifie que l'email est unique
            Inscription.objects.create(email=email)
            sujet = "Ta newsletter Stand-UP"
            html_message = render_to_string("email.html", {"username": "Dieumerci"})
            message_txt = strip_tags(html_message)  # Version texte en cas d'affichage limité
            sender = EMAIL_HOST_USER
            recipient = [email]
            send_mail(sujet, message_txt, sender, recipient, html_message=html_message)
            return redirect('thank_you')

    return redirect('index')












def thank_you(request):
    return render(request, 'thank_you.html')


def unsubscribe(request, email):
    subscriber = get_object_or_404(Inscription, email=email)
    subscriber.delete()
    return HttpResponse("Vous êtes désinscrit avec succès.")



def custom_404(request, exception):
    return render(request, '404.html', status=404)


def traduction(request):
    return render(request, "traduction.html",)

def index(request):
    return render(request, "index.html")

def apropos(request):
    return render(request, "apropos.html")

def realisation(request):
    return render(request, "realisation.html")

def realisation1(request):
    return render(request, "realisation1.html")

def realisation2(request):
    return render(request, "realisation2.html")

def service(request):
    return render(request, "service.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"""Nom: {name} \n 
        Email: {email} 
        \n \n 
        Message: \n {message}"""
        context={
            "nom":name,
            "email":email,
            "message":message
        }
        sujet = subject
        html_message = render_to_string("email1.html", context)
        message_txt = strip_tags(html_message)  # Version texte en cas d'affichage limité
        sender = EMAIL_HOST_USER
        recipient = [EMAIL_HOST_USER]
        send_mail(sujet, message_txt, sender, recipient, html_message=html_message)
        return render(request, "contact.html", {"merci":"merci d'avoir contacter Stand-Up"})
    return render(request, "contact.html")

def nots(request):
    return render(request, "404.html")


def equipe(request):
    return render(request, "equipe.html")
def article(request):
    return render(request, "article.html")
def emploi(request):
    return render(request, "emploi.html")