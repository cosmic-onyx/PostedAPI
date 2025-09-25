from django.contrib import admin

from post.models import Article, Comment, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'content', 'created_at')
    list_filter = ('user',)
    search_fields = ('title', 'content')
    ordering = ('created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'article', 'content', 'created_at')
    list_filter = ('user',)
    search_fields = ('content',)
    ordering = ('created_at',)


admin.site.register(Category)