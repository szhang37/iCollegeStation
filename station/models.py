from django.db import models

# Create your models here.
class School(models.Model):
    s_id = models.CharField(max_length=100, unique="True", primary_key = 'True')
    schoolname = models.CharField(max_length=300)
    schoolimg = models.CharField(max_length=400)
    schoollink = models.CharField(max_length=300)
    intro = models.TextField()
    
class Category(models.Model):
    cat_id = models.CharField(max_length=100, unique="True", primary_key = 'True')
    catname = models.CharField(max_length=100)
    catlink = models.CharField(max_length=200)   

class Catcnt(models.Model):
    cat = models.ForeignKey(Category, to_field = 'cat_id', primary_key=True)
    count = models.IntegerField()


class Site(models.Model):
    sitename = models.CharField(max_length = 50)
    link = models.CharField(max_length = 50)
    intro = models.TextField()

class Course(models.Model):
    c_id = models.CharField(max_length=100, unique="True", primary_key = 'True')
    lecturer = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    imglink = models.CharField(max_length=400)
    courselink = models.CharField(max_length=400)
    intro = models.TextField()
    subtitle = models.TextField()
    starttime = models.DateField()
    cat = models.ForeignKey(Category, to_field = 'cat_id')
    s = models.ForeignKey(School, to_field = 's_id')
    site = models.ForeignKey(Site)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    c = models.ForeignKey(Course)
    content = models.TextField()
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    
