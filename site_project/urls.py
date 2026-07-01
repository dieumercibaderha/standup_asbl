"""
URL configuration for site_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404
from site_app.views import *
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'site_app.views.custom_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('apropos', apropos, name="apropos"),
    path('realisation', realisation, name="realisation"),
    path('realisation1', realisation1, name="realisation1"),
    path('realisation2', realisation2, name="realisation2"),
    path('service', service, name="service"),
    path('contact', contact, name="contact"),
   
    
    path('equipe', equipe, name="equipe"),
    path('article', article, name="article"),
    
    path('emploi', emploi, name="emploi"),
    path('thank-you/', thank_you, name='thank_you'),
    path('subscribe/', subscribe, name='subscribe'),
    path('send-newsletter/', send_newsletter, name='send_newsletter'),
    path('unsubscribe/<str:email>/', unsubscribe, name='unsubscribe'),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

