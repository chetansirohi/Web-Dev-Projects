from django.db import models

class Hero(models.Model):
    name= models.CharField(max_length=60) #to store strings
    alias= models.CharField(max_length=60) #to store strings

    def __str__(self):
        return self.name
