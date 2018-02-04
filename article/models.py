from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)
    number_of_articles = models.IntegerField(default=0, blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Categories'


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    number_of_views = models.PositiveIntegerField(default=0, blank=True, null=True)
    image = models.ImageField()
    publish = models.BooleanField(default=True)
    block_comment = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('products:detail', kwargs={'slug': self.slug})

