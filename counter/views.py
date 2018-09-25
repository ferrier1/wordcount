from django.shortcuts import render
from .models import Word
from django.template import Context, Template


def dashboard(request):
    words = Word.objects.all()
    x = [(word.word, word.count) for word in words]
    x.sort(key=lambda a: a[1])
    x.reverse()
    d = {w:n for w,n in enumerate(x, 1)}
    return render(request, 'counter/dashboard.html', {'words': d})
