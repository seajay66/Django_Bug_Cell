"""tese_seajay URL Configuration

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
from shu import views
from shu2 import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cellphone/', views.cellphone),
    path('add/', views.add),
    path('delete_ce/', views.delete_ce),
    path('edit/', views.edit),
    path('ajax1/', views.ajax1),
    path('ajax2/', views.ajax2),
    path('index.html/', views.index),
    path('index1.html/', views.index1),
    path('index2.html/', views.index2),
    path('f1.html/', v2.f1),
]
