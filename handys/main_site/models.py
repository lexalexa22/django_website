from django.db import models
from django.urls import reverse
import json

class Smartphones(models.Model):
    post_title = models.CharField(max_length=255)
    post_content = models.TextField()
    slug = models.SlugField(unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    changing_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    image = models.CharField(max_length=255, null=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, default=1)
    tags = models.CharField(max_length=1000, default='[]')

    def get_tags(self):
        tags = self.tags
        return json.loads(tags)

    def set_tags(self, arg):
        self.tags = arg




    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug_adress': self.slug})

    class Meta():
        verbose_name = 'Смартфоны'
        verbose_name_plural = 'Смартфоны'
        ordering = ('id',)

class Tags(models.Model):
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta():
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
