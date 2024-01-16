from os import name
from platform import architecture
from django.db import models
from django.shortcuts import render

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.TimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name
    
class Construction(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='constructions')
    site_name = models.CharField(max_length=255)
    in_charge = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.project.id} - Construction"

class Architecture(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='architectures')
    name = models.CharField(max_length=255)
    design = models.CharField(max_length=255)
    area = models.FloatField()
    height = models.IntegerField()
    floor = models.IntegerField()

    def __str__(self):
        return f"{self.project.id}-{self.name}"
