from django import template
from django.conf import settings
from urllib.parse import urljoin

register = template.Library()


@register.simple_tag
def mediapath(image):
    if image:
        return urljoin(settings.MEDIA_URL, str(image))
    return ""
