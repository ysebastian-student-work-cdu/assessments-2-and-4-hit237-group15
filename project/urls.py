"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('recipe/', views.recipe, name='recipe'),
    path('add_recipe', views.ADD_recipe, name='add_recipe'),
    path('delete_recipe/<str:id>', views.DELETE_recipe, name='delete_recipe'),
    path('update_recipe/<str:id>', views.UPDATE_recipe, name='update_recipe'), 
    path('update_done_recipe/<str:id>', views.UPDATE_done_recipe, name='update_done_recipe'), 
    path('food_item/', views.food_item, name='food_item'),
    path('add_fooditem', views.ADD_fooditem, name='add_fooditem'),
    path('delete_fooditem/<str:id>', views.DELETE_fooditem, name='delete_fooditem'),
    path('update_done_fooditem/<str:id>', views.UPDATE_done_fooditem, name='update_done_fooditem'), 
    path('update_fooditem/<str:id>', views.UPDATE_fooditem, name='update_fooditem'), 



]
