from django import template


register = template.Library()

BAD_WORDS = ('Редиска', 'редиска')


@register.filter()
def censor(value):
    return value[0] + '*' * (len(value) - 1)
