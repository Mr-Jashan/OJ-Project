from django.urls import path
from . import views

urlpatterns = [
   path('add_question', views.add_question, name='add_question'),
   path('add_testcase', views.add_testcase, name='add_testcase')
]