from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save, post_save

from .utils import create_slug


class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)
    number_of_articles = models.IntegerField(default=0, blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category

    def get_absolute_categories_url(self):
        return reverse('articles:category', kwargs={'category': self.category})

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

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'slug': self.slug})


def pre_save_article_reciver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


def post_save_article_receiver(sender, instance, created, *args, **kwargs):
    if created:
        qs = Article.objects.filter(slug=instance)
        if qs.exists() and qs.count() == 1:
            article = qs.first()
            category = Category.objects.get(category=article.category)
            category.number_of_articles += 1
            category.save()


pre_save.connect(pre_save_article_reciver, sender=Article)
post_save.connect(post_save_article_receiver, sender=Article)
