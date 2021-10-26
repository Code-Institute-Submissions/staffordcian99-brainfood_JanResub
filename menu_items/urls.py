from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_menu_items, name='all_items')
]
