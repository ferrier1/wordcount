from django.db import models

class Word(models.Model):
    hash = models.CharField(max_length=200)
    word = models.CharField(max_length=200)
    number_of = models.IntegerField()

    def __str__(self):
        return self.word
