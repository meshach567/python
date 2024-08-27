from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'name': 'Amaka',
        'age': '24',
        'place': 'Lagos'
        }
    return render(request, 'index.html', context)
