from django import template
from django.utils.html import mark_safe

from markdown import markdown


register = template.Library()


@register.filter(name='markdown')
def md(markup):
    html = mark_safe(markdown(markup, safe_mode='escape'))
    return html