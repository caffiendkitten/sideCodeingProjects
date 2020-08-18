# this file is responsible for storing functions?

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')