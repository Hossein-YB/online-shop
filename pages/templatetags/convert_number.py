from django import template

register = template.Library()


@register.filter
def english_to_persian(value):
    value = str(value)
    number = value.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
    return value.translate(number)

