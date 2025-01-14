from django.urls import path
from . import views

urlpatterns = [
   #  path('register/', ),
   # path('register/', views.user_registration, name='user_registration'),
   # path('login/', views.user_login, name='login'),
   path('home/', views.home_page, name='home'),
   path('submit/',views.submit, name='submit'),
]