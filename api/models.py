from django.db import models

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    
    #to make the database in django admin show by it's name
    def __str__(self):
        return self.name
