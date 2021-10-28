from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_menu_items, name='all_items'),
    path('<menu_item_id>', views.item_detail, name='item_detail'),
]
