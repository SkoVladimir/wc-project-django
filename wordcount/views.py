from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def eggs(request):
    return HttpResponse('Eggs are great')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1
        else:
            #add to the dict.
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    context = {'context': fulltext, 'count': len(wordlist), 'sortedwords': worddictionary.items()}
    return render(request, 'count.html', context)