from django.urls import path
from . import views

urlpatterns = [
   #  path('register/', ),
   path('register/', views.user_registration, name='user_registration'),
   path('login/', views.user_login, name='login'),
   path('logout/', views.user_logout, name='logout'),
   
]