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


def food_item(request):
    re = FoodItems.objects.all()
    context = {
        're' : re,
    }
    return render(request, 'fooditems.html', context)


def ADD_fooditem(request):
    if request.method == "POST":
        itemID = request.POST.get('itemID')
        name = request.POST.get('name')
        category = request.POST.get('category')
        expiryDate = request.POST.get('expiryDate')

        re = FoodItems(
            itemID = itemID,
            name = name,
            category = category,
            expiryDate = expiryDate
        )
        re.save()
        messages.info(request, "Food item Added")

    return redirect('food_item')

def DELETE_fooditem(request, id):
    re = FoodItems.objects.filter(id = id)
    re.delete()

    context = {
        're' : re,
    }
    messages.info(request, "Food item Deleted")

    return redirect('food_item')



def UPDATE_done_fooditem(request, id):
    sel_fooditem = FoodItems.objects.get(id = id)
    sel_fooditem.itemID = request.POST.get('itemID')
    sel_fooditem.name = request.POST.get('name')
    sel_fooditem.category = request.POST.get('category')
    sel_fooditem.expiryDate = request.POST.get('expiryDate')
    sel_fooditem.save()
    messages.info(request, "Food item updated")

    return redirect('food_item')

def UPDATE_fooditem(request, id):
    sel_fooditem = FoodItems.objects.get(id = id)
    re = FoodItems.objects.all()
    context = {
        'sel_fooditem' : sel_fooditem,
        're' : re,
    }
    
    return render(request, 'fooditems.html', context)


def food_waste(request):
    re = FoodWaste.objects.all()
    context = {
        're' : re,
    }
    return render(request, 'foodwaste.html', context)

def ADD_foodwaste(request):
    if request.method == "POST":
        wasteID = request.POST.get('wasteID')
        itemID = request.POST.get('itemID')
        quantityWasted = request.POST.get('quantityWasted')
        reason = request.POST.get('reason')

        re = FoodWaste(
            wasteID = wasteID,
            itemID = itemID,
            quantityWasted = quantityWasted,
            reason = reason
        )
        re.save()
        messages.info(request, "Food waste Added")

    return redirect('food_waste')



def DELETE_foodwaste(request, id):
    re = FoodWaste.objects.filter(id = id)
    re.delete()

    context = {
        're' : re,
    }
    messages.info(request, "Food waste Deleted")

    return redirect('food_waste')


def UPDATE_done_foodwaste(request, id):
    sel_foodwaste = FoodWaste.objects.get(id = id)
    sel_foodwaste.wasteID = request.POST.get('wasteID')
    sel_foodwaste.itemID = request.POST.get('itemID')
    sel_foodwaste.quantityWasted = request.POST.get('quantityWasted')
    sel_foodwaste.reason = request.POST.get('reason')
    sel_foodwaste.save()
    messages.info(request, "Food waste updated")

    return redirect('food_waste')

def UPDATE_foodwaste(request, id):
    sel_foodwaste = FoodWaste.objects.get(id = id)
    re = FoodWaste.objects.all()
    context = {
        'sel_foodwaste' : sel_foodwaste,
        're' : re,
    }
    
    return render(request, 'foodwaste.html', context)