from django.utils.text import slugify


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    article = instance.__class__
    qs = article.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = '%s-%s' % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug
