from django.contrib import admin
from .models import Question, Choice
# Register your models here.

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        ('Data information', {'fields': ['pub_date']}),
        (None,               {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin)

