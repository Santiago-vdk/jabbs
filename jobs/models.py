# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models

from ckeditor.fields import RichTextField

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['name']
        
    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

        
class Company(models.Model):
    name = models.CharField(max_length=32)
    logo = models.URLField(max_length=200)
    video = models.URLField(max_length=200)
    website = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    
    def __str__(self):
        return self.name

class Job(models.Model):
    school = models.ManyToManyField(School, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    pub_date = models.DateTimeField('publish date')
    exp_date = models.DateTimeField('expiry date')
    job_location = models.CharField(max_length=24)
    job_position = models.CharField(max_length=24)
    job_type = models.CharField(max_length=12)
    job_requirements = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, blank=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name
