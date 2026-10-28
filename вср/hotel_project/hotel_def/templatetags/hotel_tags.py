from django import template
from ..models import Room

register = template.Library()

@register.simple_tag
def total_rooms():
    return Room.objects.count()


@register.filter
def add_rub(value):
    return f"{value} руб."



@register.inclusion_tag('tags/popular_rooms.html')
def show_popular_rooms(count=3):
    rooms = Room.objects.order_by('price_per_night')[:count]
    return {'rooms':rooms}

