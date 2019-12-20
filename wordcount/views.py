from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html', {'hithere': 'This is me'})


def about(request):
    return render(request, 'about.html')


def count(request):
    fullText = request.GET['fullText']
    wordList = fullText.split()
    worddictionary = {}
    for word in wordList:
        if word in worddictionary:
            # Increase Count
            worddictionary[word] += 1
        else:
            # Add to the dictionary
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(),
                         key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fullText': fullText, 'count': len(wordList), 'sortedwords': sortedwords})
