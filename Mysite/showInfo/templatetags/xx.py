from django.template import Library


register = Library()



@register.filter
def my_lower(value, args):
    return value + args


@register.simple_tag
def my_tag(value, a, b, c):
    return value + a[0] + b[0] + c[0]