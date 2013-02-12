from content.models import Film, Article, MediaEntry, ID
from django.contrib import admin

def publish(modeladmin, request, queryset):
    queryset.update(is_published=True)
publish.short_description = "Publish selected articles"

def unpublish(modeladmin, request, queryset):
    queryset.update(is_published=False)
unpublish.short_description = "Mark selected articles as draft"

def invalidate(modeladmin, request, queryset):
    queryset.update(is_valid=False)
publish.short_description = "Invalidate selected ids"

def validate(modeladmin, request, queryset):
    queryset.update(is_valid=True)
publish.short_description = "Make selected IDs valid"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'date_published', 'is_published')
    actions = [publish, unpublish]

class FilmAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'tags')

class IDAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'is_valid')
    actions = [validate, invalidate]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(ID, IDAdmin)
admin.site.register(MediaEntry)
