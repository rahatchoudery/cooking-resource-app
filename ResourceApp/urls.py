from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.HomePage),
    path('subject/', views.SubjectPage),
    path('results/', views.result1),
]
