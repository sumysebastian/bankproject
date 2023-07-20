from django.contrib import admin

# Register your models here.
from . models import District,Branches
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(District,DistrictAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Branches,BranchAdmin)