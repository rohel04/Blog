from tkinter import CASCADE
from turtle import title
from django.db import models
from datetime import date
from django.contrib.auth.models import User
from category.models import Category


# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.TextField()
    image=models.ImageField(upload_to="post_img")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateField(default=date.today())

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    date=models.DateField(default=date.today())

    def __str__(self):
        return self.user