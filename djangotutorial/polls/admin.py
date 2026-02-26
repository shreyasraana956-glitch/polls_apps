from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    """Inline admin for Choice — allows editing choices on the Question page."""
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """Custom admin for Question with fieldsets and inline choices."""
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
