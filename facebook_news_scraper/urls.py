"""facebook_news_scraper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('api/pages', views.get_pages, name="api_get_pages"),
    path('api/posts/all', views.get_all_posts, name="api_get_all_posts"),
    path('api/posts', views.get_posts, name="api_get_posts"),
    path('interactives/top_posts', views.top_posts, name="interactive_top_posts")
]
