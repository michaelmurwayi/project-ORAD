from os import name
from platform import architecture
from django.db import models
from django.shortcuts import render

# Create your models here.

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    description = models.TextField()
    start_date = models.TimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name
    
class Construction(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    site_name = models.CharField()
    in_charge = models.CharField()
    construction_id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.project.id} - Construction"
    

class Architecture(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    design = models.CharField()
    area = models.FloatField()
    height = models.IntegerField()
    floor = models.IntegerField()
    architecture_id = models.AutoField(primary_key=True)

