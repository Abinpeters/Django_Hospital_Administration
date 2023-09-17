from django.db import models

# Create your models here.
class Docdetails(models.Model):
    name=models.CharField(max_length=50, default='0000000')
    specialized=models.CharField(max_length=100, default='aaaa')
    address=models.CharField(max_length=100, default='0000000')
    number=models.IntegerField(max_length=50, default='0000000')
    email=models.EmailField(max_length=255, default='abc@gmail.com')
    username=models.CharField(max_length=50, default='0000000')
    password=models.IntegerField(max_length=255, default='000000')
    def __str__(self):
        return self.name
class Patdetails(models.Model):
    name=models.CharField(max_length=50, default='0000000')
    age=models.CharField(max_length=50, default='0000000')
    disease=models.CharField(max_length=100, default='aaa')
    doctor=models.CharField(max_length=200, default='aaa')
    address=models.CharField(max_length=100, default='0000000')
    number=models.CharField(max_length=50, default='0000000')
    email=models.EmailField(max_length=255, default='abc@gmail.com')
    feedback=models.CharField(max_length = 250,default="aaaaa")
    
    