from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.
def home(request):
    return render(request, 'simple_app/base.html' )

def search(request):
    data_search = request.POST.get('search')
    data = {
        'data_search': data_search
    }
    return render(request, 'simple_app/new_search.html', data)