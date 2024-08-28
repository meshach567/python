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

    box1 = Box()
    box1.id = 0
    box1.name = 'Fast'
    box1.details = 'Our Service'

    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Easy to Used'
    feature1.details = 'Our Service'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Easy to implement'
    feature2.details = 'Our Service'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Easy to work with'
    feature3.details = 'Our Service'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Easy to integrate'
    feature4.details = 'Our Service'

    features = [feature1, feature2, feature3, feature4]
    return render(request, 'index.html', { 'box': box1, 'features': features})

# def counter(request):
#     text = request.POST['text']
#     amount_of_words = len(text.split())
#     return render(request, 'counter.html', {'amount': amount_of_words})
