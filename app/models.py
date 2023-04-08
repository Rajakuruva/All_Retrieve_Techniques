from django.db import models

# Create your models here.

class Topic(models.Model):
    Topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.Topic_name

class Webpage(models.Model):
    Topic_name=models.ForeignKey(Topic,models.CASCADE)
    name=models.CharField(max_length=100)
    State=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,models.CASCADE)
    Author=models.CharField(max_length=100)
    Dates=models.DateField() 

    def __str__(self):
        return self.Author