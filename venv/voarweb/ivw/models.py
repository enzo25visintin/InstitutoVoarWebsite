from django.db import models

# Create your models here.
class User(models.Model):
    Status_choices = [('A', 'Active'), ('I','Inactive'),]
    
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    telephone_number = models.CharField(max_length=15)
    company = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=Status_choices, default='1')


    def __str__(self):
        return self.name

