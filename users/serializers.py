from rest_framework import serializers
from .models import Users
from snippets.serializers import UsersSerializer
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'email', 'first_name', 'last_name', 'password',]
