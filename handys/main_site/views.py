import json

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.db.models import Q
from random import shuffle
import re
from main_site.forms import *
from main_site.models import Smartphones, Category, Tags
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator


def index(request):
    current_page_number = request.GET.get('page')
    if current_page_number == '1':
        return redirect('home')
    if current_page_number is None:
        current_page_number = 1
    current_page_number = int(current_page_number)
    all_posts = Smartphones.objects.all()
    categories = Category.objects.all()

    paginator = Paginator(all_posts, 9)
    current_page = paginator.page(current_page_number)
    posts = current_page.object_list
    previous_page_number = current_page_number - 1
    pre_previous_page_number = current_page_number - 2
    next_page_number = current_page_number + 1
    next_next_page_number = current_page_number + 2
    pagination = [pre_previous_page_number, previous_page_number, current_page_number, next_page_number,
                  next_next_page_number]

    context = {
        'posts': posts,
        'categories': categories,
        'current_page': current_page_number,
        'pagination': pagination,
        'last_page': paginator.num_pages
    }
    return render(request, 'main_site/index.html', context=context)







def viewpost(request, slug_adress):
    content = Smartphones.objects.get(slug=slug_adress)
    title = content.post_title
    tags = eval(content.tags)
    tag1 = tags[0]
    tag2 = tags[1]
    all_tags = Tags.objects.all()
    similar = Smartphones.objects.filter(Q(post_title__contains=tag1) | Q(post_title__contains=tag2)).order_by('?')
    #similar = Smartphones.objects.filter(Q(tags__contains=tag1) | Q(tags__contains=tag2)).order_by('?')

    similar = similar[:12]
    context = {
        'content': content,
        'tag1': tag1,
        'tag2': tag2,
        'similar': similar,
        'all_tags': all_tags
    }
    return render(request, 'main_site/post.html', context=context)

def view_category(request, cat_id):
    current_page_number = request.GET.get('page')
    if current_page_number == '1':
        return redirect(f'/category/{cat_id}')
    if current_page_number is None:
        current_page_number = 1
    else:
        current_page_number = int(current_page_number)
    categories = Category.objects.all()
    all_posts = Smartphones.objects.filter(cat_id=cat_id)

    #Pagination
    paginator = Paginator(all_posts, 9)
    current_page = paginator.page(current_page_number)
    posts = current_page.object_list
    previous_page_number = current_page_number-1
    pre_previous_page_number = current_page_number-2
    next_page_number = current_page_number+1
    next_next_page_number = current_page_number+2
    pagination = [pre_previous_page_number, previous_page_number, current_page_number, next_page_number, next_next_page_number]

    if cat_id>len(categories):
        return Http404(request, 'не найдено')
    context = {
            'categories': categories,
            'current_category': cat_id,
            'current_page': current_page_number,
            'all_posts': posts,
            'pagination': pagination,
            'last_page': paginator.num_pages
            }

    return render(request, 'main_site/category.html', context=context)

def other_page(request, number):
    if number == 1:
        return redirect('home')
    num = (number-1)*10-(number-1)
    num_to = num+9
    posts = Smartphones.objects.all()[num:num_to]
    pattern = r'<img src="(.*?)"'
    images = dict()
    for post in posts:
        content = post.post_content
        image = re.search(pattern, content)
        if image:
            images[post.slug] = image.group(1).replace('"', '')
        else:
            images[
                post.slug] = 'https://fdn.gsmarena.com/imgroot/reviews/23/vivo-v27/lifestyle/-1200w5/gsmarena_017.jpg'

    context = {
        'posts': posts,
        'current_category': 0,
        'categories': Category.objects.all(),
        'images': images,
        'current_page': number
    }
    return render(request, 'main_site/other.html', context=context)

def other_page_cats(request, cat_id, number):
    if number == 1:
        posts = Smartphones.objects.filter(cat_id=cat_id)[:9]
    else:
        num = (number-1)*10-(number-1)
        num_to = num+9
        posts = Smartphones.objects.filter(cat_id=cat_id)[num:num_to]
    pattern = r'<img src="(.*?)"'
    images = dict()
    for post in posts:
        content = post.post_content
        image = re.search(pattern, content)
        if image:
            images[post.slug] = image.group(1).replace('"', '')
        else:
            images[
                post.slug] = 'https://fdn.gsmarena.com/imgroot/reviews/23/vivo-v27/lifestyle/-1200w5/gsmarena_017.jpg'

    context = {
        'posts': posts,
        'current_category': cat_id,
        'categories': Category.objects.all(),
        'images': images,
        'current_page': number
    }
    return render(request, 'main_site/other.html', context=context)

def tags(request, query):
    query = query.replace('%20', ' ')
    all_posts = Smartphones.objects.filter(post_title__icontains=query)
    context = {
        'all_posts': all_posts,
        'tag': query
    }
    return render(request, 'main_site/tag.html', context=context)

def registragion(request):
    form = UserRegister
    context = {
        'registragion_form': form
    }
    return render(request, 'main_site/registration.html', context=context)

def creating_tags(request):
    all_posts = Smartphones.objects.all()
    for post in all_posts:
        title = post.post_title
        try:
            if ':' in title:
                phone1 = title.split(':')[0].split(' vs ')[0]
                phone2 = title.split(':')[0].split(' vs ')[1]
                post.tags = [phone1, phone2]
                post.save()
                continue
            if '.' in title:
                phone1 = title.split('.')[0].split(' vs ')[0]
                phone2 = title.split('.')[0].split(' vs ')[1]
                post.tags = [phone1, phone2]
                post.save()
        except:
            continue

    return HttpResponse('Готово')
def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1>'
                                f'{exception}')