from datetime import datetime
from django import template

register = template.Library()

@register.filter
def difference_in_days(date1, date2):
    if date1 and date2:
        difference = date1 - date2
        return difference.days
    else:
        return None

@register.filter
def mult(a, b):
    return a * b

@register.filter
def print_date(date):
    return date.strftime('%d/%m/%Y')

