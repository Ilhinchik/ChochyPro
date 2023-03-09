from unittest.util import _MAX_LENGTH
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    money = models.IntegerField(default=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=50) # Название анкеты

    reason = models.TextField() # Причина обращения
    details = models.TextField() # Подробности
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE)


    def __str__(self):
        return self.title