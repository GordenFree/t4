from django.db import models

class Bboard(models.Model):
    title = models.CharField(max_length=50, verbose_name='Модель автомобиля')
    content = models.TextField(null=True, blank=True, verbose_name='Описание авто')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена автомобиля')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    class Meta:
        verbose_name='Обьявление'
        verbose_name_plural='Обьявления'
        ordering = ['-published']

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index = True, verbose_name = 'Название')
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']