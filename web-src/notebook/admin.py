from django.contrib import admin
from .models import NoteBook


class NotebookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'owner', 'created_at']}),
        ('Info', {'fields': ['id', 'description', 'private', 'updated_at']}),
    ]
    list_display = ('name', 'owner', 'created_at')
    list_filter = ('private', )
    filter_horizontal = ()


admin.site.register(NoteBook, NotebookAdmin)
