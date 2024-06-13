from django.contrib import admin
from django.urls import path, re_path
from django.urls import include
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ItemSitemap


sitemaps = {
    'itmes': ItemSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('cart/', include('cart.urls')),
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
