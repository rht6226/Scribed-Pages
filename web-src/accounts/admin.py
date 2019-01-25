from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User
from django.contrib.auth.models import Permission


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'bio', 'profile_image')}),
    )
    ordering = ('username', 'email', 'first_name', 'last_name')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(Permission)
admin.site.unregister(Group)