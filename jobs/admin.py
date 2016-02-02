from django.contrib import admin

from django import forms

from .models import Job, Company, Tag, School


class JobAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'company', 'pub_date', 'exp_date')
    search_fields = ['name', 'company']
    list_filter = ('company','school','pub_date','exp_date')


admin.site.register(Job, JobAdmin)
admin.site.register(Company)
admin.site.register(Tag)
admin.site.register(School)


# Register your models here.
