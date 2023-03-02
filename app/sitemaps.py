from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home','about','contact-us','services','webinar']

    def location(self, item):
        return reverse(item)