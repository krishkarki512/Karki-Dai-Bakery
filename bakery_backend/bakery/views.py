from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cake, Newsletter
from django.shortcuts import render

def home(request):
    cakes = Cake.objects.all()  # Get all cakes from the database
    return render(request, 'index.html', {'cakes': cakes})