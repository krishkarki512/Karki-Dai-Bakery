from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cake, Newsletter
from django.shortcuts import render

def home(request):
    cakes = Cake.objects.all()  # Get all cakes from the database
    return render(request, 'home.html', {'cakes': cakes})

def search_cakes(request):
    query = request.GET.get('q', '')

    if query:
        cakes = Cake.objects.filter(name__icontains=query)
    else:
        cakes = Cake.objects.all()

    return render(request, 'search.html', {
        'cakes': cakes,
        'query': query
    })