# coding: utf-8

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.utils.safestring import mark_safe

from content.models import Article


class LatestEntriesFeed(Feed):
    title = "cramur.me posts"
    link = "/feed/"
    description = "cramur.me blog entries. Updates rarely"
    feed_type = Atom1Feed
    item_author_name = "cra"
    item_author_email = "c6h10o5@gmail.com"
    feed_copyright = "Copyright (c) WTFPL, cra"
    #title_template = "feeds/latest_title.html"
    #description_template = "feeds/latest_description.html"

    def items(self):
        return Article.objects.filter(is_published=True).order_by('-date_published')[:7]

    def item_title(self, item):
        return item.title + u" -- %s " % item.summary

    def item_description(self, item):
        return mark_safe(item.content)

    def item_pubdate(self, item):
        return item.date_published

