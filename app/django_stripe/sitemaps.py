from django.contrib.sitemaps import Sitemap
from shop.models import Item

class ItemSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Item.objects.all()

    #def lastmod(self, obj):
    #    return obj.updated_at
