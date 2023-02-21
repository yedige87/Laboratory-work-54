from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Наименование продукта')
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Описание продукта')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Стоимость продукта')
    photo = models.CharField(max_length=200, null=False, blank=False, verbose_name='Изображение продукта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    deleted_at = models.DateTimeField(auto_now=True, verbose_name="Время удаления")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категория")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('info', kwargs={'info_id': self.pk})

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ['price', 'title']


class Category(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Наименование продукта')
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Описание продукта')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']