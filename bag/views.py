from django.shortcuts import render

# Create your views here.
def view_bag(request):
    """ A view for the shopping bag page """

    return render(request, 'bag/bag.html')
