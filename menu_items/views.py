from django.shortcuts import render, get_object_or_404
from .models import MenuItem

# Create your views here.

def all_menu_items(request):
    """ A view for all menu items """

    menu_items = MenuItem.objects.all()

    context = {
        'menu_items': menu_items,
    }

    return render(request, 'menu_items/menu.html', context)

def item_details(request, menu_item_id):
    """ A view for item descriptions """

    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)

    context = {
        'menu_item': menu_item,
    }

    return render(request, 'menu_items/item_details.html', context)
