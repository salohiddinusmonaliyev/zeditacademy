from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    kasb = models.CharField(max_length=50)


    def __str__(self):
        return self.first_name

class Article(models.Model):
    title = models.CharField(max_length=50)
    mavzu = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
