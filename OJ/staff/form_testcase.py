from django import forms
from pages.models import testcase

class add_a_testcase (forms.ModelForm):
   
   class Meta:
      model = testcase
      fields = ["question_id", "tc_input", "tc_output"]