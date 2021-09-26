from django.db import models

# Create your models here.
class acc(models.Model):
    email=models.CharField(max_length=255)
    name=models.CharField(max_length=20)
    message=models.TextField()
    address=models.DateTimeField(auto_now_add = True)
