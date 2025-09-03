from django.db import models

# Create your models here.
class PageVist(models.Model):
    # db ->table
    # id -> primary key -> 1,2,3,... autofield
    
    
    path = models.TextField(null=True)
    timstamp =models.DateTimeField(auto_now_add=True)
    