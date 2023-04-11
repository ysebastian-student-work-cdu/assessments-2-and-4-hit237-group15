from django.urls import path
from item.views import HelloView, ItemListView, ItemDetailView

urlpatterns = [
    path('', HelloView.as_view(), name='home'),
    path('item/', ItemListView.as_view(), name='item'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
]
