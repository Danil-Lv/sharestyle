from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *


class StyleItemsInline(admin.TabularInline):
    model = Style.items.through
    extra = 1


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    """Стили"""
    list_display = ('title', 'author',)
    list_display_links = ('title',)
    list_filter = ('author',)
    inlines = [StyleItemsInline]
    exclude = ('items',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Одежда"""

    list_display = ('title', 'price', 'show_image', 'author', 'created_at')
    list_display_links = ('title', 'price')
    search_fields = ('title',)

    # Вывод фотографии в админке
    def show_image(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return None

    show_image.short_description = 'Изображение'


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Review)

admin.site.site_title = 'ShareStyle'
admin.site.site_header = 'ShareStyle'
