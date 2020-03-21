from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'simple_app/base.html' )

def search(request):
    return render(request, 'base.html')