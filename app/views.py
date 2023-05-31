from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from app.models import User, Audit_Record, Food_Items
# Create your views here.
def app(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def user(request):
    re = User.objects.all()
    context = {
        're' : re,
    }
    return render(request, 'user.html', context)

def ADD_user(request):
    if request.method == "POST":
        userid = request.POST.get('userid')
        name = request.POST.get('name')
        email = request.POST.get('email')
        role = request.POST.get('role')

        re = User(
            userid = userid,
            name = name,
            email = email,
            role = role
        )
        re.save()
        messages.info(request, "user Added")

    return redirect('user')

def DELETE_user(request, id):
    re = User.objects.filter(id = id)
    re.delete()

    context = {
        're' : re,
    }
    messages.info(request, "user Deleted")

    return redirect('user')

def UPDATE_user(request, id):
    sel_recipe = User.objects.get(id = id)
    re = User.objects.all()
    context = {
        'sel_recipe' : sel_recipe,
        're' : re,
    }
    
    return render(request, 'user.html', context)

def UPDATE_done_user(request, id):
    sel_recipe = User.objects.get(id = id)
    sel_recipe.userid = request.POST.get('userid')
    sel_recipe.name = request.POST.get('name')
    sel_recipe.email = request.POST.get('email')
    sel_recipe.role = request.POST.get('role')
    sel_recipe.save()
    messages.info(request, "user updated")

    return redirect('user')


def audit_record(request):
    re = Audit_Record.objects.all()
    context = {
        're' : re,
    }
    return render(request, 'audit_record.html', context)


def ADD_audit_record(request):
    if request.method == "POST":
        food_item = request.POST.get('food_item')
        location = request.POST.get('location')
        audit_date = request.POST.get('audit_date')
        waste_quantity = request.POST.get('waste_quantity')

        re = Audit_Record(
            food_item = food_item,
            location = location,
            audit_date = audit_date,
            waste_quantity = waste_quantity
        )
        re.save()
        messages.info(request, "Record Added")

    return redirect('audit_record')

def DELETE_audit_record(request, id):
    re = Audit_Record.objects.filter(id = id)
    re.delete()

    context = {
        're' : re,
    }
    messages.info(request, "Record Deleted")

    return redirect('audit_record')



def UPDATE_done_audit_record(request, id):
    sel_fooditem = Audit_Record.objects.get(id = id)
    sel_fooditem.food_item = request.POST.get('food_item')
    sel_fooditem.location = request.POST.get('location')
    sel_fooditem.audit_date = request.POST.get('audit_date')
    sel_fooditem.waste_quantity = request.POST.get('waste_quantity')
    sel_fooditem.save()
    messages.info(request, "Record updated")

    return redirect('audit_record')

def UPDATE_audit_record(request, id):
    sel_fooditem = Audit_Record.objects.get(id = id)
    re = Audit_Record.objects.all()
    context = {
        'sel_fooditem' : sel_fooditem,
        're' : re,
    }
    
    return render(request, 'audit_record.html', context)


def food_items(request):
    re = Food_Items.objects.all()
    context = {
        're' : re,
    }
    return render(request, 'food_item.html', context)

def ADD_food_item(request):
    if request.method == "POST":
        name = request.POST.get('name')
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        reason = request.POST.get('reason')

        re = Food_Items(
            name = name,
            category = category,
            quantity = quantity,
            reason = reason
        )
        re.save()
        messages.info(request, "Food Item Added")

    return redirect('food_items')



def DELETE_food_item(request, id):
    re = Food_Items.objects.filter(id = id)
    re.delete()

    context = {
        're' : re,
    }
    messages.info(request, "Food Item Deleted")

    return redirect('food_items')


def UPDATE_done_food_item(request, id):
    sel_foodwaste = Food_Items.objects.get(id = id)
    sel_foodwaste.name = request.POST.get('name')
    sel_foodwaste.category = request.POST.get('category')
    sel_foodwaste.quantity = request.POST.get('quantity')
    sel_foodwaste.reason = request.POST.get('reason')
    sel_foodwaste.save()
    messages.info(request, "Food Item updated")

    return redirect('food_items')

def UPDATE_food_item(request, id):
    sel_foodwaste = Food_Items.objects.get(id = id)
    re = Food_Items.objects.all()
    context = {
        'sel_foodwaste' : sel_foodwaste,
        're' : re,
    }
    
    return render(request, 'food_item.html', context)