from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class HistoricalPeriod(models.Model):
    """Исторические периоды"""
    PERIODS = [
        ('stone', 'Каменный век'),
        ('bronze', 'Бронзовый век'),
        ('iron', 'Железный век'),
        ('medieval', 'Средние века'),
        ('modern', 'Новое время'),
    ]
    name = models.CharField(max_length=100, choices=PERIODS)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Исторический период'
        verbose_name_plural = 'Исторические периоды'
    
    def __str__(self):
        return f"{self.get_name_display()} ({self.start_year} - {self.end_year or 'наши дни'})"


class HistoricalFact(models.Model):
    """Интересные исторические факты"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    period = models.ForeignKey(HistoricalPeriod, on_delete=models.CASCADE)
    year = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='facts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Исторический факт'
        verbose_name_plural = 'Исторические факты'
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    """Комментарии к фактам"""
    fact = models.ForeignKey(HistoricalFact, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
    
    def __str__(self):
        return f"Комментарий от {self.author} к {self.fact}"


class SavedArticle(models.Model):
    """Сохраненные статьи пользователя"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fact = models.ForeignKey(HistoricalFact, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'fact')
        verbose_name = 'Сохраненная статья'
        verbose_name_plural = 'Сохраненные статьи'
    
    def __str__(self):
        return f"{self.user} сохранил {self.fact}"
