from django.contrib import admin
from .models import *

class View_smartphones(admin.ModelAdmin):
    list_display = ('id', 'post_title', 'creation_date', 'changing_date', 'cat', 'is_published')
    list_display_links = ('post_title',)
    list_editable = ('is_published',)
    list_filter = ('creation_date', 'changing_date', 'id', 'is_published')


class View_category(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

admin.site.register(Smartphones, View_smartphones)
admin.site.register(Category)