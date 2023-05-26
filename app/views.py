from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from app.models import Recipe, FoodItems, FoodWaste
# Create your views here.
def app(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def recipe(request):
    re = Recipe.objects.all()
    context = {
        're' : re,
    }
    return render(request, 'recipe.html', context)

def ADD_recipe(request):
    if request.method == "POST":
        recipeID = request.POST.get('recipeID')
        name = request.POST.get('name')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')

        re = Recipe(
            recipeID = recipeID,
            name = name,
            ingredients = ingredients,
            instructions = instructions
        )
        re.save()
        messages.info(request, "Recipe Added")

    return redirect('recipe')

def DELETE_recipe(request, id):
    re = Recipe.objects.filter(id = id)
    re.delete()

    context = {
        're' : re,
    }
    messages.info(request, "Recipe Deleted")

    return redirect('recipe')

def UPDATE_recipe(request, id):
    sel_recipe = Recipe.objects.get(id = id)
    re = Recipe.objects.all()
    context = {
        'sel_recipe' : sel_recipe,
        're' : re,
    }
    
    return render(request, 'recipe.html', context)

def UPDATE_done_recipe(request, id):
    sel_recipe = Recipe.objects.get(id = id)
    sel_recipe.recipeID = request.POST.get('recipeID')
    sel_recipe.name = request.POST.get('name')
    sel_recipe.ingredients = request.POST.get('ingredients')
    sel_recipe.instructions = request.POST.get('instructions')
    sel_recipe.save()
    messages.info(request, "Recipe updated")

    
    return redirect('recipe')