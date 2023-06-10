from django import template
from main_site.models import *

register = template.Library()

@register.simple_tag(name='all_posts_')
def all_posts(pk=None):
    if not pk:
        return Smartphones.objects.all()[:5]
    else:
        return Smartphones.objects.filter(pk=pk)[:5]

@register.inclusion_tag('main_site/list_categories.html', name='category_list')
def category_list(current_category=None):
    cats = Category.objects.all()
    if not current_category:
        return {'cats': cats}
    else:
        return {'cats': cats, 'current_category': current_category}

@register.inclusion_tag(r'main_site/navigation.html', name='navigation')
def navigation(current_page=0, current_category=0):
    if current_category != 0:
        all_posts = Smartphones.objects.filter(cat_id=current_category)
    else:
        all_posts = Smartphones.objects.all()
    number_of_pages = round(len(all_posts)/9)
    links = []
    if current_page>=3:
        links.append(current_page-2)
        links.append(current_page-1)
        links.append(current_page)
        links.append(current_page+1)
        links.append(current_page+2)
    else:
        for i in range(2, 7):
            links.append(i)
    return {'links': links,
            'current_page': current_page,
            'last_page': number_of_pages,
            'current_category': current_category}

@register.inclusion_tag('main_site/list_of_tags.html', name='list_of_tags')
def list_of_tags():
    all_tags = Tags.objects.all()
    return {
        'all_tags': all_tags
    }