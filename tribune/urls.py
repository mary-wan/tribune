"""tribune URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from news import views as news_views

import news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('news.urls')),
    path('register/',news_views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    url(r'^tinymce/', include('tinymce.urls')),
    
    
    # path('logout/', news_views.logout, {"next_page": '/'}), 
    
    # path('accounts/', include('django_registration.backends.activation.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('logout/', views.logout, {"next_page": '/'}), 
    # url(r'^admin/', admin.site.urls),
    # url(r'^news/',include('news.urls'))
    
    # path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # change default template path

]
