from django.contrib import admin
from .models import Pass
# Register your models here.


class PassAdmin(admin.ModelAdmin):
    list_display = ('id','email' ,'password', 'addDate', 'deleted')


admin.site.register(Pass, PassAdmin)