"""
URL configuration for my_research_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
import os 
# my_research_project/urls.py

from django.contrib import admin
from django.urls import path, include  # Make sure 'include' is imported!

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Route all root requests directly over to your research agent application layout
    path('', include('research_agent.urls')), 
]# my_research_project/urls.py


