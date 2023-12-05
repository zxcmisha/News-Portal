from django import template


register = template.Library()

BAD_WORDS = ('Редиска', 'редиска')


@register.filter()
def censor(value):
    return value[0] + '*' * (len(value) - 1)

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()
