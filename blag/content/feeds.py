# coding: utf-8

from django.contrib.syndication.views import Feed

from content.models import Article


class LatestEntriesFeed(Feed):
    title = "cramur.me posts"
    link = "/feed/"
    description = "cramur.me blog entries. Updates rarely"

    def items(self):
        return Article.objects.filter(is_published=True).order_by('-date_published')[:7]

    def item_title(self, item):
        return item.title + u" -- %s" % item.summary

    def item_description(self, item):
        return item.content

