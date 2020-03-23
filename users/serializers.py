from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import BorrowedBook

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'first_name', 'last_name', 'phone']

class BorrowedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBook
        fields = ['book_title', 'user', 'phone_number', 'date_of_Pickup', 'date_of_return']

class UserBorrowedBooksSerializer(serializers.ModelSerializer):
    borrowed_books = serializers.PrimaryKeyRelatedField(many=True, queryset=BorrowedBook.objects.all())

    class Meta:
        model = get_user_model()
        fields = ['borrowed_books']
