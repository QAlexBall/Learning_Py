from django.contrib import admin

# Register your models here.

from .models import Article, Comment, User
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_id', 'article_title', 'article_created_time')
    fieldsets = [
        ('Data information', {'fields': ['article_created_time']}),
        ('Title',            {'fields': ['article_title']}),
        ('Context',          {'fields': ['article_context']})
    ]
    inlines = [CommentInline]
    list_filter = ['article_created_time']
    search_fields = ['title']

admin.site.register(Article, ArticleAdmin)
admin.site.register(User)