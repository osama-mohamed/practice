from django.db import models
from .utils import code_generator, create_shortcode
from django.conf import settings
from django.core.urlresolvers import reverse
from .validators import validate_url, validate_domain


SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)


class URLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(URLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = URL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_codes += 1
        return 'New Codes made : {i}'.format(i=new_codes)


class URL(models.Model):
    url = models.CharField(max_length=250, validators=[validate_url, validate_domain])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = URLManager()
    # some_random = URLManager()


    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        if not 'http' in self.url:
            self.url = 'http://' + self.url
        super(URL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def get_absolute_url(self):
        return 'http://localhost:8000/{shortcode}'.format(shortcode=self.shortcode)

    def get_short_url(self):
        url_path = reverse('scode', kwargs={'shortcode': self.shortcode})
        return 'http://localhost:8000' + url_path


