# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models

from ckeditor.fields import RichTextField
from geoposition.fields import GeopositionField
from django.contrib.auth.models import User
from django.utils import timezone

import bcrypt
import requests

def time_now():
    now = datetime.now()

def get_token():
    request = requests.get('http://randomword.setgetgo.com/get.php')
    word = request.text
    print("")
    print('\x1b[0m' + "Hashing the word "  + '\033[93m' + word + '\x1b[0m' + ". Please wait..." + '\033[92m')
    print('\033[92m')
    password = word.encode(encoding='UTF-8',errors='strict')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))
    return hashed

class InvitationCode(models.Model):
    code = models.CharField(default=get_token,blank = False, max_length = 60, unique=True, verbose_name=(u"Invitation code"))
    is_used = models.BooleanField(default=False, verbose_name=(u"Used?"))
    is_issued = models.BooleanField(default=True, verbose_name=(u"Issued?"))
    user = models.ForeignKey(User, blank=True, null=True)
    issued_date = models.DateTimeField(blank=False, default=timezone.now, verbose_name=(u"Issued on"))
    used_date = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name=(u"Used on"))

    def __str__(self):
        return self.code
    

#Tag Model
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['name']
        
    def __str__(self):
        return self.name

#Job Type Model - Should be Freelance, Full Time, etc...
class Type(models.Model):
    name = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.name

#School Model
class School(models.Model):
    name = models.CharField(max_length=50, unique=True)
    initials = models.CharField(max_length=3,unique=True)

    def __str__(self):
        return self.name

#Company Model        
class Company(models.Model):
    name = models.CharField(max_length=32)
    slogan = models.CharField(max_length=32)
    logo = models.URLField(max_length=200)
    video = models.URLField(max_length=200)
    website = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)

    class Meta:
        verbose_name_plural = "companies"
    
    def __str__(self):
        return self.name

#Job Model
class Job(models.Model):
    school = models.ManyToManyField(School, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    pub_date = models.DateTimeField('publish date', default=timezone.now, editable = False)
    exp_date = models.DateTimeField('expiry date')
    #job_location = models.CharField(max_length=24)
    job_position = models.CharField(max_length=24)
    location_name = models.CharField(max_length=100)
    location_position = GeopositionField()
    
    #job_type = models.CharField(max_length=24)
    #job_requirements = models.CharField(max_length=200)
    #tags = models.ManyToManyField(Tag, blank=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name

