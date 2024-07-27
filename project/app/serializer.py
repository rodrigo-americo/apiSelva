from rest_framework import serializers
from .models import *


class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['userName', 'password', 'active', 'datecreatedAt']
