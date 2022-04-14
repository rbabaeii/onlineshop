from email.mime import image
from pyexpat import model
from django.db import models
from uuid import uuid4
# Create your models here.
class Food(models.Model):
    id = models.CharField(max_length=200 , primary_key=True , default= uuid4)
    name = models.CharField(max_length=100 , null= True , blank= True)
    price = models.FloatField(max_length= 20)
    description = models.TextField(max_length=100 , null= False , blank=False)
    image = models.ImageField()
    def __str__(self) -> str:
        return self.name
class New_order(models.Model):
    id = models.CharField(max_length=200 , primary_key=True , default= uuid4)
    foods = models.ManyToManyField(Food)
    data = models.JSONField()
    def __str__(self) -> str:
        return f"{self.id}"