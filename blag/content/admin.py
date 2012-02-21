from content.models import MediaEntry, Article
from django.contrib import admin

def publish(modeladmin, request, queryset):
    queryset.update(is_published=True)
publish.short_description = "Publish selected articles"

def unpublish(modeladmin, request, queryset):
    queryset.update(is_published=False)
unpublish.short_description = "Mark selected articles as draft"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'date_published', 'is_published')
    actions = [publish, unpublish]

admin.site.register(Article, ArticleAdmin)
admin.site.register(MediaEntry)
