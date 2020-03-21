from rest_framework import serializers
from .models import Book, BorrowedBook

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'author', 'year_of_release',]

class BorrowedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBook
        fields = ['book_title', 'user', 'phone_number', 'date_of_Pickup', 'date_of_return']
