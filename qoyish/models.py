from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Video(models.Model):
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="video")
# class Add_Model(models.Model):
#     boolean=models.BooleanField(default=True,verbose_name="True False")
#     char=models.CharField(verbose_name='Name',max_length=100,help_text='Add help text')
#     positive_int=models.PositiveIntegerField()
#     slug=models.SlugField(blank=True)
#     # phone=PhoneNumberField()