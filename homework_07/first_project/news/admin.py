from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import News, Category, Comment


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','description']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment']


admin.site.unregister(User)


@admin.register(User)
class CustomAdminUser(UserAdmin):
    readonly_fields = [
        'date_joined',
    ]
    def get_form(self,request,obj = None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['username'].disabled = True

        return form







