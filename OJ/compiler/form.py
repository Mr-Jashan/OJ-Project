from django import forms
from compiler.models import CodeSubmission 

lang_choice = [
   ("py", "Python"),
   ("cpp", "C++" ),
]

class codesubmissionform (forms.ModelForm):
   language = forms.ChoiceField(choices=lang_choice)
   
   class Meta:
      model = CodeSubmission
      fields = ["language", "code", "input_data"]