from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Article(models.Model):
    source = models.CharField(verbose_name='source', max_length=200, null=True, blank=True)
    author = models.CharField(verbose_name='author', max_length=200, null=True, blank=True)
    publisher = models.ForeignKey(User, verbose_name='author', related_name='articles',
                                  on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(verbose_name='title', max_length=200, null=True, blank=True)
    description = models.TextField(verbose_name='description', null=True, blank=True)
    url = models.URLField(verbose_name='article url', null=True, blank=True)
    url_to_image = models.URLField(verbose_name='url to image', null=True, blank=True)
    published_at = models.DateTimeField(verbose_name='published at', null=True, blank=True)
    content = models.TextField(verbose_name='content', null=True, blank=True)

    class Meta:
        ordering = ('-published_at',)


class FavoriteArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-added_at',)
