from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Group
'''
@admin.register(User)
class UserAdminConfig(UserAdmin):
    ordering = ('full_name',)
    list_display = ('full_name','cpf', 'date_of_birth', 'had_covid_last_month',)
'''
    
admin.site.register(User)
admin.site.register(Group)