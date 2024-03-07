from django import template
import random

register = template.Library()

@register.filter
def shuffle(value):
    try:
        return random.choice(value)
    
    except IndexError:
        return value

