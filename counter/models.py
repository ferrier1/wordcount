from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=200)
    count = models.IntegerField()

    def __str__(self):
        return self.word
