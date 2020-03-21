from django.db import models
from django.conf import settings
from django.utils import timezone

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
    users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    phone_number = models.IntegerField()
    date_of_Pickup = models.DateTimeField()
    date_of_return = models.DateTimeField()

    def _str_(self):
        return self.title

    """
    sure go i will, i'm not going man but i'm waiting for you

    BABA CONTINUE! don't forget to do the serializer & views for this as well.
    User model also needs serializer and views as well
    also we're going to need to send back a token for the user model
    """
