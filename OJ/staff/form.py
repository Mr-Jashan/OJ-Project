from django import forms
from pages.models import question_list 

# lang_choice = [
#    ("py", "Python"),
#    ("cpp", "C++" ),
# ]

class add_a_question (forms.ModelForm):
   # language = forms.ChoiceField(choices=lang_choice)
   
   class Meta:
      model = question_list
      fields = ["question_name", "question_statement", "difficulty"]