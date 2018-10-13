from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=200)
    number_of = models.IntegerField(default=1)


    def __str__(self):
        return self.word


class Hash(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    hash = models.CharField(max_length=200)

    def __str__(self):
        return self.hash
