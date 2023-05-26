from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from app.models import Recipe, FoodItems, FoodWaste
# Create your views here.
def app(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def index2(request):
    return 1        #test function 
