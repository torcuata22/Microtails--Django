"""microtails URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from pages.views import home_view, about_view, login_view, register_view, write_view, read_view, faq_view
from tales.views import tale_detail_view, tale_create_view

urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('login/', login_view, name='login page'),
    path('register/', register_view, name='registration page'),
    path('write/', write_view, name='create a new tale'),
    path('read/', read_view, name='read our tales' ),
    path('faq/', faq_view, name='faq' ),
    path('tales/details.html', tale_detail_view, name='tale'),
     path('tales/tale_create.html', tale_create_view, name='create tale'),
    path('admin/', admin.site.urls),
]
