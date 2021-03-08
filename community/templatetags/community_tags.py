from django import template
register = template.Library()

@register.filter
def is_applied(post, user):
    return post.is_applied(user)