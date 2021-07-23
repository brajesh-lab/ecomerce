from django.db import models

# Create your models here.
class Product(models.Model):
     photo  = models.ImageField(upload_to = 'statics')
     name = models.CharField(max_length = 20)
     weight = models.IntegerField(null=True)
     price  = models.CharField(max_length = 10)
     created_at = models.DateTimeField(auto_now_add=True , null= True)
     updated_at = models.DateField( auto_now_add=True , null = True)


     def __str__(self):
          return self.name