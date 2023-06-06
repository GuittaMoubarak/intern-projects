from django.contrib import admin
from .models import Editor
# Register your models here.


class EditorAdmin(admin.ModelAdmin):
    list_display = ('id', 'body')


admin.site.register(Editor, EditorAdmin)


