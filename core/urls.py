from django.contrib import admin
from django.urls import path, include
from django.contrib.admin.views.decorators import staff_member_required

app_name = 'core'

admin.site.login = staff_member_required(admin.site.login, login_url='')

urlpatterns = [
    path('admin/', admin.site.urls  ),
    path("", include('pages.urls'), name ='pages'),
]
