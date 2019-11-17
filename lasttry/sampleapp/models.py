from django.db import models
from django.conf import  settings

# search using user.objects.get(name='harshal')
class user(models.Model):
    name = models.CharField(max_length=50)
    photo=models.ImageField(blank=True,upload_to='images/',null=True)
    username = models.CharField(max_length=50,unique=True)
    pwd = models.CharField(max_length=50)
    details = models.TextField()
    qual = models.CharField(null=True,blank=True,max_length=50)

class fileModel(models.Model):
    username = models.CharField(max_length = 50)
    file = models.FileField()
    title = models.CharField(max_length = 100)
    timestamp = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)

class comments(models.Model):
    username = models.CharField(max_length = 50)
    postid = models.IntegerField()
    comment = models.TextField()