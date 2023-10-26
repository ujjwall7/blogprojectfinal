from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    Categoryname=models.CharField(max_length=200)

    @staticmethod 
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.Categoryname


class Blog(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    Title = models.CharField(max_length=250)
    Description= models.TextField()
    Image = models.ImageField(null=True,blank=True)
    Pub_date = models.DateTimeField('date published', auto_now_add=True)
    Author= models.CharField(max_length=50)

    def __str__(self):
        return self.Title


    @staticmethod 
    def get_all_Blog():
        return Blog.objects.all()


    @staticmethod 
    def get_all_Blog_by_id(category_id):
        if category_id: 
            return Blog.objects.filter(category=category_id) 
        else:
            return Blog.get_all_Blog();


