# research_agent/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Map the root domain straight to your main dashboard UI
    path('', views.research_dashboard, name='research_dashboard'),
    
    # AJAX endpoints triggered by the frontend JavaScript buttons
    path('summarize/', views.summarize_paper, name='summarize_paper'),
    path('hypothesize/', views.suggest_hypothesis, name='suggest_hypothesis'),
]