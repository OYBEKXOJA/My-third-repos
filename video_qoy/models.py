from django.db import models

# Create your models here.
class Qoyish(models.Model):
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to='vidos')