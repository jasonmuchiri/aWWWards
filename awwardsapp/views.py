from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt


# Create your views here.
def index(request):
    return render(request, 'index.html')

def search_results(request):
    return render(request, 'search.html')    