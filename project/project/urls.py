

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import *
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UsuarioView.as_view(), name='qualquercoisa')
]
