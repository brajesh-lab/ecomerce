from django.db import models
from datetime import  date

# Create your models here.
class users(models.Model):
    f_name = models.CharField(max_length = 20)
    l_name = models.CharField(max_length =10)
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 10)

    def __str__(self):
        return self.f_name

class Post(models.Model):
     userid = models.ForeignKey(users, on_delete = models.CASCADE)
     text  = models.TextField(max_length = 150)
     created_at = models.CharField(max_length =10,null=True)
     updated_at = models.CharField(max_length =10,null= True )

     