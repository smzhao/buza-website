from django.contrib import admin

from project.accounts.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    # Register your models here.
    list_display = ['user', 'school']


admin.site.register(Profile, ProfileAdmin)
