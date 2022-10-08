from django.db import models

# Create your models here.
class Story(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title

        
class Image(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=500)
    path = models.CharField(max_length=1000)