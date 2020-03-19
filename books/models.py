#from django.contrib.postgres.fields import ArrayField
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    author = models.CharField(max_length=120)
    year_of_release = models.IntegerField()
    #category = ArrayField(models.CharField(max_length=200), blank=True)

    def _str_(self):
        return self.title
