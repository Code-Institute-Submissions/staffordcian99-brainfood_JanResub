from django import template

register = template.Library()


def calc_subtotal(price, quantity):
    return price * quantity


register.filter('calc_subtotal', calc_subtotal)
