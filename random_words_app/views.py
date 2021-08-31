from django.shortcuts import render, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    request.session["random_count"] = 0
    return render(request, 'random_words_app/index.html')

def random(request):
    word = get_random_string(length=14)
    context = {
        'random_words_app':word
    }
    request.session["random_count"] += 1
    return render(request, 'random_words_app/index.html', context)

def reset(request):
    request.session["random_count"] = 0
    return render(request, 'random_words_app/index.html')
