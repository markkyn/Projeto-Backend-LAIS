from django.contrib import admin
from django.urls import path, include

app_name = 'core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
    path("", include('pages.urls'), name ='pages'),
]
