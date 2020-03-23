from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Book(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    author = models.CharField(max_length=120)
    year_of_release = models.IntegerField()
    category = models.TextField() # fiction,non-fiction,

    def _str_(self):
        return self.title

class BorrowedBook(models.Model):
    book_title = models.CharField(max_length=120)
    user = models.ForeignKey(get_user_model(), related_name='borrowed_books', on_delete=models.CASCADE)
    date_of_Pickup = models.DateTimeField()
    date_of_return = models.DateTimeField()

    def _str_(self):
        return self.title
