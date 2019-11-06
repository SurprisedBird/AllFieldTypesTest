from django.contrib import admin
from fields.models import AllFieldsTypes
# Register your models here.

class FieldsAdmin(admin.ModelAdmin):
    list_display = ('date', 'uid')

admin.site.register(AllFieldsTypes, FieldsAdmin)