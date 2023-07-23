from django import template
from django.conf import settings
from urllib.parse import urljoin

register = template.Library()


@register.filter
def media_path(image):
    if image:
        return urljoin(settings.MEDIA_URL, image.url)
    return ""


@register.simple_tag
def media_path(image):
    if image:
        if not isinstance(image.url, str):
            raise TypeError("image.url is not a string")
        return urljoin(str(settings.MEDIA_URL), str(image.url))
    return ""
