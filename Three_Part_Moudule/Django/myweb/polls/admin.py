from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Data information', {'fields': ['pub_date']}),
        (None,               {'fields': ['question_text']}),
    ]
admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)

