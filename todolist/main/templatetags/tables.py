from django import template
from ..models import Tables

register = template.Library()

@register.simple_tag
def tables_categories():
    return Tables.objects.all()