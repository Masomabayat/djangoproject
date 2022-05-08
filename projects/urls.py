from lib2to3.pygram import pattern_grammar
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),  
]