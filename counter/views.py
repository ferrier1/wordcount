from django.shortcuts import render
from .models import Word, Hash
from django.template import Context, Template
from newsapi import NewsApiClient
import hashlib


def dashboard(request):
    words = Word.objects.all()
    #counters = Counter.objects.all()
    x = [(word.word, word.number_of) for word in words]
    #x = zip(words.values_list('word', flat=True), counters.values_list('word_count', flat=True))
    x2 = list(x)
    x2.sort(key=lambda a: a[1])
    x2.reverse()
    d = {w:n for w,n in enumerate(x2, 1)}
    update()
    return render(request, 'counter/dashboard.html', {'words': d})

def update():
    current_words = Word()
    current_hashes = Hash()
    api = NewsApiClient(api_key='1f7851a84b9d499797e5518bee76b285')
    bbc = api.get_top_headlines(sources='bbc-news')['articles']
    for x in bbc:
        data = {hashlib.md5(str.encode(x['title'])+str.encode(x['publishedAt'])).hexdigest():
        x['description'].split()}
        for key in data:
            for word in data[key]:
                print(word, key)
                if Hash.objects.filter(hash=key).exists():
                    print("skipping")
                elif Word.objects.filter(word=word).exists():
                    counter = Word.objects.get(word=word)
                    counter.number_of += 1
                    counter.save()
                    test = Word.objects.get(word=word)
                    current_hashes.word = test
                    current_hashes.hash = key
                    current_hashes.save()
                else:
                    current_words.pk = None
                    current_words.word = word
                    current_words.save()






"""
            for word in wordset:
                if Word.objects.filter(word=word).exists():
                    for item in Word.objects.filter(word=word):
                        print(item.word, item.number_of, word)
"""
