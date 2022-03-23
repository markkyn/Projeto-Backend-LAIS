from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

app_name = 'core'

urlpatterns = [
    path('admin/', admin.site.urls  ),
    path("", include('pages.urls'), name ='pages'),
]
