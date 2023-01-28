from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from profiles.models import User


# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'show_image_outside')
    fieldsets = (
        (None, {"fields": ("username", "password", "image", "show_image_inside", "is_stylist")}),
        (("Личная информация"), {"fields": ("first_name", "last_name", "email", "instagram", "telegram", "whatsapp")}),
        (('Подписки'), {'fields': ('subscriptions',)}),
        (
            ("Права доступа"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Даты"), {"fields": ("last_login", "date_joined")}),
    )
    readonly_fields = ('show_image_inside',)

    def show_image_inside(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='140' />".format(obj.image.url))
        return None

    show_image_inside.__name__ = 'Фото пользователя'

    def show_image_outside(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return None

    show_image_outside.__name__ = 'Фото пользователя'
