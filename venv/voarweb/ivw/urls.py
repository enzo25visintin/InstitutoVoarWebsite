# ivw/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/about', views.about, name='about'),

    path('users/', views.user_list, name='user_list'),
    path('new/', views.user_create, name='user_create'),
    path('edit/<int:pk>/', views.user_update, name='user_update'),

]