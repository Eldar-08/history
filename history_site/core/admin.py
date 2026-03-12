from django.contrib import admin
from .models import HistoricalPeriod, HistoricalFact, Comment, SavedArticle

# Register your models here.

@admin.register(HistoricalPeriod)
class HistoricalPeriodAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_year', 'end_year')
    search_fields = ('name',)

@admin.register(HistoricalFact)
class HistoricalFactAdmin(admin.ModelAdmin):
    list_display = ('title', 'period', 'year', 'views', 'created_at')
    list_filter = ('period', 'year')
    search_fields = ('title', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('fact', 'author', 'created_at')
    search_fields = ('text', 'author__username')

@admin.register(SavedArticle)
class SavedArticleAdmin(admin.ModelAdmin):
    list_display = ('user', 'fact', 'saved_at')
    search_fields = ('user__username', 'fact__title')
