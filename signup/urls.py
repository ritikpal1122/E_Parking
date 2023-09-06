from django.contrib import admin
from django.urls import path,include
from signup import views
urlpatterns = [
    path('login/', views.login),
    path('saveaccount/', views.saveaccount),
]
