from django import template

register = template.Library()


@register.filter
def comment_tags(comments):
    return comments.filter(active=True)


@register.filter
def count_comment_tags(comments):
    return comments.filter(active=True).count()
