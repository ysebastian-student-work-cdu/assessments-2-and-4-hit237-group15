from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

# Create your views here.
def app(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')
