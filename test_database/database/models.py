from os import name
from platform import architecture
from django.db import models
from django.shortcuts import render

# Create your models here.

class Project(models.Model):
    name = models.CharField()
    description = models.TextField()
    start_date = models.TimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name
    
class Construction(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    site_name = models.CharField()
    in_charge = models.CharField()
    construction_id = models.OneToManyField(Project, related_name='project_construction_id')
    
    def __str__(self):
        return f"{self.id} - {self.name}"

class Architecture(models.Model):
    name = models.CharField()
    design = models.CharField()
    area = models.FloatField()
    height = models.IntegerField()
    floor = models.IntegerField()
    architecture_id = models.OneToManyField(Project, related_name='project_architecture_id')

    def __str__(self):
        return f"{self.id}-{self.name}"

