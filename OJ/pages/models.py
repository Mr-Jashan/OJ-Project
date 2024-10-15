from django.db import models
from django.contrib.auth.admin import User

# Create your models here.
class question_list(models.Model):
   question_id = models.AutoField(primary_key=True)
   question_name = models.CharField(max_length=255)
   question_statement = models.TextField()
   difficulty_choices = [
      ("easy", "Easy"),
      ("mediam", "Mediam"),
      ("hard", "Hard"),
   ]
   difficulty = models.CharField(max_length=6, choices=difficulty_choices, default="easy")
   
   def __str__ (self):
      return f"{self.question_id})   {self.question_name}"
   
class testcase(models.Model):
   question_id = models.ForeignKey(question_list, on_delete=models.CASCADE)
   tc_input = models.TextField()
   tc_output = models.TextField() 
   
class code_record(models.Model):
   username = models.ForeignKey(User, on_delete=models.CASCADE)
   language = models.CharField(max_length=15)
   code = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)
   
   def __str__ (self):
      return f"{self.username} {self.language} {self.created_at}"
    
   class Meta:
      ordering = ['-created_at'] 
      
class code_check(models.Model):
   username = models.ForeignKey(User, on_delete=models.CASCADE)
   question_id = models.ForeignKey(question_list, on_delete=models.CASCADE)
   is_accepted = models.BooleanField(default=False)
   
   def __str__ (self):
      return f"{self.username} {self.is_accepted}"
   
   
