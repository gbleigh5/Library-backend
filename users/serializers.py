from rest_framework import serializers
from django.contrib.auth import get_user_model
from books.models import BorrowedBook

class UserSerializer(serializers.ModelSerializer):
    borrowed_books = serializers.PrimaryKeyRelatedField(many=True, queryset=BorrowedBook.objects.all())

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'borrowed_books']
