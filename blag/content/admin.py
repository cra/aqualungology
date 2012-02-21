from content.models import MediaEntry, Article
from django.contrib import admin

class ArticleAdmin(admin.ModelAdmin):
    fields = ['slug', 'title', 'date_published', 'is_draft']

admin.site.register(Article, ArticleAdmin)
admin.site.register(MediaEntry)
