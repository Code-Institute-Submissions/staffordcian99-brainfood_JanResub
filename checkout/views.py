from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JqFc9IDxcY27dnmR4VBfeUXYhlo178X7idGrZaGzYNFtpDTTSW4KVB83mIH3i3ba5R86sqOQq1Q2I4ppSqaqcjA00QOG6U5kb',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
