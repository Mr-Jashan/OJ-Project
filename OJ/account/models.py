from django.db import models
from django.contrib.auth.admin import User

# class user_register(models.Model):
#     username = models.CharField(max_length=25)
#     email = models.CharField(max_length=35)
#     password = models.CharField(max_length=15)

#     def __str__(self):
#         return self.username

class profile (models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   points = models.FloatField(default=0)
    
   def __str__ (self):
      return self.user.username