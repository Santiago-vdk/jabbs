from django.contrib import admin

from django import forms

from .models import Job, Company, Tag, School, Type, InvitationCode


class JobAdmin(admin.ModelAdmin):
    exclude = ('creator',)
    list_display = ( 'name', 'company', 'pub_date', 'exp_date', 'creator')
    search_fields = ['name', 'company', 'user']
    list_filter = ('company','school','pub_date','exp_date', 'creator')

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(JobAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.creator.id:
            return False
        return True

    def queryset(self, request):
        if request.user.is_superuser:
            return Jobs.objects.all()
        return Jobs.objects.filter(creator=request.user)
   
    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        obj.save()


        
class CompanyAdmin(admin.ModelAdmin):
    exclude = ('creator',)
    def has_change_permission(self, request, obj=None):
        has_class_permission = super(CompanyAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.creator.id:
            return False
        return True
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        obj.save()
        
    def queryset(self, request):
        if request.user.is_superuser:
            return Company.objects.all()
        return Company.objects.filter(creator=request.user)
     
class InvitationCodeAdmin(admin.ModelAdmin):
    list_display = ( 'code', 'user', 'is_used', 'used_date', 'issued_date')
    list_filter = ( 'user', 'issued_date',)
    readonly_fields=('code',)
    
    def has_add_permission(self, request):
        return False


admin.site.register(Job, JobAdmin)
admin.site.register(Company, CompanyAdmin)
#admin.site.register(Tag)
admin.site.register(School)
admin.site.register(Type)
admin.site.register(InvitationCode, InvitationCodeAdmin)
