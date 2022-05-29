#  hello/urls.py

from django.shortcuts import render
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "portfolio"

urlpatterns = [
    path('index', views.index_view),
    path('home', views.home_page_view, name='home'),
    path('about', views.about_view, name='sobre'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
