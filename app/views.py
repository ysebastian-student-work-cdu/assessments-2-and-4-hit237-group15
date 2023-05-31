from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from app.models import User
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

