from .views import *
from django.urls import path
from django.contrib.sitemaps import Sitemap #class for sitemap creating
from django.contrib.sitemaps.views import sitemap #view_function for sitemap creating

#creating Class and dict for sitemap
class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Smartphones.objects.filter(is_published=True)

sitemaps = {'blog': BlogSitemap}
#####

urlpatterns = [
    path('', index, name='home'),
    path('post/<slug:slug_adress>', viewpost, name='post'),
    path('category/<int:cat_id>', view_category, name='category'),
    path('page/<int:number>', other_page, name='other page'),
    path('tag/<str:query>', tags, name='tags'),
    path('registration/', registragion, name='registration'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap")
]