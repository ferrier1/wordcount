from django.shortcuts import render
from .models import Word
from django.template import Context, Template
from newsapi import NewsApiClient
import hashlib


def dashboard(request):
    words = Word.objects.all()
    x = [(word.word, word.count) for word in words]
    x.sort(key=lambda a: a[1])
    x.reverse()
    d = {w:n for w,n in enumerate(x, 1)}
    update()
    return render(request, 'counter/dashboard.html', {'words': d})

def update():
    currnet_words = Word.objects.all()
    api = NewsApiClient(api_key='1f7851a84b9d499797e5518bee76b285')
    bbc = api.get_top_headlines(sources='bbc-news')['articles']
    for x in bbc:
        data = {hashlib.md5(str.encode(x['title'])+str.encode(x['publishedAt'])).hexdigest():
        x['description'].split()}
        #print(data)
        for wordset in data.values():
            for word in wordset:
                #print(word)
                if Word.objects.filter(word=word).exists():
                    print(currnet_words.word)
