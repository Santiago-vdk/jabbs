from django.contrib import admin

from django import forms

from .models import Job, Company, Tag


class JobAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'company', 'pub_date', 'exp_date')
    search_fields = ['name', 'company']
    list_filter = ('company','pub_date','exp_date')


admin.site.register(Job, JobAdmin)
admin.site.register(Company)
admin.site.register(Tag)


# Register your models here.
