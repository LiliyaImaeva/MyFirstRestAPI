from rest_framework import serializers
from . import models


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Roles
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = '__all__'
