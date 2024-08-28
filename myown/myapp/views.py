from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature, Box


# Create your views here.

def index(request):
    # context = {
    #     'name': 'Amaka',
    #     'age': '24',
    #     'place': 'Lagos'
    #     }

    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our Service'

    box1 = Box()
    box1.id = 0
    box1.icon = '<i class="bi bi-buildings"></i>'
    box1.name = 'Easy to Used'
    return render(request, 'index.html', { 'feature': feature1})

# def counter(request):
#     text = request.POST['text']
#     amount_of_words = len(text.split())
#     return render(request, 'counter.html', {'amount': amount_of_words})
