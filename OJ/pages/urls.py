from django.urls import path
from . import views

urlpatterns = [
   path('list_questions/', views.list, name='question_list'),
   path('question/<int:question_id>', views.q_solve, name = 'question_detail'),
   path('home/', views.homepage, name='homepage'),
   path('leaderbord/', views.leaderbord, name='leaderbord'),
   path('submissions/', views.submissions, name = 'submissions')
]