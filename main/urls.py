from django.urls import path 
from . import views

urlpatterns = [
    path('home/', views.homes, name='homes'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
   
]
