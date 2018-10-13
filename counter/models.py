from django.db import models

class Hash(models.Model):
    hash = models.CharField(max_length=200)

    def __str__(self):
        return self.hash

class Word(models.Model):
    word = models.CharField(max_length=200)
    number_of = models.IntegerField(default=1)
    hash = models.ForeignKey(Hash, on_delete=models.CASCADE)

    def __str__(self):
        return self.word
