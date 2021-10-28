from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import MenuItem

# Create your views here.


def all_menu_items(request):
    """ A view for all menu items """

    menu_items = MenuItem.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('menu_items'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            menu_items = menu_items.filter(queries)
    context = {
        'menu_items': menu_items,
        'search_term': query,
    }

    return render(request, 'menu_items/menu.html', context)


def item_detail(request, menu_item_id):
    """ A view to show individual item details """

    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)

    context = {
        'menu_item': menu_item,
    }

    return render(request, 'menu_items/item_detail.html', context)

