from django.template import library
import re
import locale

register = library.Library()

@register.filter()
def price_format(string):
    locale.setlocale(locale.LC_ALL, '')
    return locale.format_string('%d', string, grouping=True)
