from django.contrib import admin
from bookmark_service.models import Bookmark

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')

# admin.site.register(Bookmark, BookmarkAdmin)