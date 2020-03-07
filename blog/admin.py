from django.contrib import admin

from blog.models import (
    Article,
    Comment,
    # Profile,
)


class CommentsInline(admin.StackedInline):
    model = Comment
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentsInline]


# class ProfileAdmin(admin.ModelAdmin):
#     pass
#

admin.site.register(Article, ArticleAdmin)
# admin.site.register(Profile, ProfileAdmin)
