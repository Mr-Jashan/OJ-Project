# from django.db import models

# # Create your models here.

# class codesubmission (models.Model):
#    language = models.CharField(max_length=15)
#    code = models.TextField()
#    input_data = models.TextField(null = True , blank=True)
#    output_data = models.TextField(null = True , blank=True)
#    timestamp = models.DateTimeField(auto_now_add=True)
   

from django.db import models

# Create your models here.

class CodeSubmission(models.Model):
    language = models.CharField(max_length=15)
    code = models.TextField()
    input_data = models.TextField(null=True, blank=True)
    output_data = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
