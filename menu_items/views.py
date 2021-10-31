from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import MenuItem, Category
from .forms import MenuItemForm

# Create your views here.


def all_menu_items(request):
    """ A view for all menu items """

    menu_items = MenuItem.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            menu_items = menu_items.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        
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
        'current_categories': categories,
    }

    return render(request, 'menu_items/menu.html', context)


def item_detail(request, menu_item_id):
    """ A view to show individual item details """

    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)

    context = {
        'menu_item': menu_item,
    }

    return render(request, 'menu_items/item_detail.html', context)


@login_required
def add_menu_item(request):
    """ Add a menu item to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added menu item!')
            return redirect(reverse('add_menu_item'))
        else:
            messages.error(request, 'Failed to add menu item. Please ensure the form is valid.')
    else:
        form = MenuItemForm()
    template = 'menu_items/add_menu_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_menu_item(request, menu_item_id):
    """ Edit a menu_item in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=menu_item)
        if form.is_valid():
            menu_item = form.save()
            messages.success(request, 'Successfully updated menu item!')
            return redirect(reverse('item_detail', args=[menu_item.id]))
        else:
            messages.error(request, 'Failed to update menu item. Please ensure the form is valid.')
    else:
        form = menu_itemForm(instance=menu_item)
        messages.info(request, f'You are editing {menu_item.name}')

    template = 'menu_items/edit_menu_item.html'
    context = {
        'form': form,
        'menu_item': menu_item,
    }

    return render(request, template, context)


@login_required
def delete_menu_item(request, menu_item_id):
    """ Delete a menu_item from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
    menu_item.delete()
    messages.success(request, 'menu item deleted!')
    return redirect(reverse('all_items'))
