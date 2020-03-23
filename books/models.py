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
