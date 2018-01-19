from django.utils.text import slugify
import random
import string


def random_srting_generator(size=12):
    return "".join([random.choice(string.ascii_letters + string.digits) for _ in range(size)])


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    klass = instance.__class__
    qs_exists = klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = '{slug}-{randomstr}'.format(
            slug=slug,
            randomstr=random_srting_generator(size=6)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug