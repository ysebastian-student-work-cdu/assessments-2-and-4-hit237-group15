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
    path('user/', views.user, name='user'),
    path('add_user', views.ADD_user, name='add_user'),
    path('delete_user/<str:id>', views.DELETE_user, name='delete_user'),
    path('update_user/<str:id>', views.UPDATE_user, name='update_user'), 
    path('update_done_user/<str:id>', views.UPDATE_done_user, name='update_done_user'), 
    path('audit_record/', views.audit_record, name='audit_record'),
    path('add_audit_record', views.ADD_audit_record, name='add_audit_record'),
    path('delete_audit_record/<str:id>', views.DELETE_audit_record, name='delete_audit_record'),
    path('update_done_audit_record/<str:id>', views.UPDATE_done_audit_record, name='update_done_audit_record'), 
    path('update_audit_record/<str:id>', views.UPDATE_audit_record, name='update_audit_record'), 
    path('food_items/', views.food_items, name='food_items'),
    path('add_food_item', views.ADD_food_item, name='add_food_item'),
    path('delete_food_item/<str:id>', views.DELETE_food_item, name='delete_food_item'),
    path('update_done_food_item/<str:id>', views.UPDATE_done_food_item, name='update_done_food_item'), 
    path('update_food_item/<str:id>', views.UPDATE_food_item, name='update_food_item'), 

]
