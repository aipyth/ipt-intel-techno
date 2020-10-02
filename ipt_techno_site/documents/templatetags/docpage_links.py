from django import template
from ..models import DocPage


register = template.Library()

@register.inclusion_tag('documents/docpage_link.html')
def get_docpages():
    pages = DocPage.objects.all()
    return {'docpages': pages}

@register.inclusion_tag('documents/collapsive_docpage_link.html')
def get_docpages_collapsive():
    pages = DocPage.objects.all()
    return {'docpages': pages}