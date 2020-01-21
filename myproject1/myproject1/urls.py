"""myproject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from userApp.views import *
from dataApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginP),
    path('p.html', show_p),
    path('tables.html', show),
    path('index.html', indexPage),
    path('register.html', zc),
    path('RegisterPage', zc),
    path('log', loginP),
    path('login.html', tc),
    path('login', loginP),
    path('Smessage', Mes),
    path('tables', refresh),
    path('admin.html', loginP),
    path('message.html', show_M),
    path('delete', delete),
    path('admin', ad),
    path('Index', index),

]
