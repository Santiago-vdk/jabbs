from django.contrib import admin

from django import forms

from .models import Job, Company, Tag, School, Type, InvitationCode


class JobAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'company', 'pub_date', 'exp_date')
    search_fields = ['name', 'company']
    list_filter = ('company','school','pub_date','exp_date')

class InvitationCodeAdmin(admin.ModelAdmin):
    list_display = ( 'code', 'user', 'is_used', 'used_date', 'issued_date')
    list_filter = ( 'user', 'issued_date',)
    readonly_fields=('code',)
    def has_add_permission(self, request):
        return False


admin.site.register(Job, JobAdmin)
admin.site.register(Company)
#admin.site.register(Tag)
admin.site.register(School)
admin.site.register(Type)
admin.site.register(InvitationCode, InvitationCodeAdmin)
