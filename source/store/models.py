from django.db import models

CATEGORY_CHOICES = [('other', 'Разное'), ('fruits', 'Фрукты'), ('vegetables', 'Овощи'), ('beverage', 'Напитки'),
                    ('bakery', 'Выпечка')]


class Products(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=15, default='other', verbose_name='Категория')
    residue = models.IntegerField(null=False, verbose_name='Остаток')
    price = models.FloatField(max_length=7, null=False, verbose_name='Цена')


def __str__(self):
    return f'{self.title} {self.description} {self.category} {self.residue} {self.price}'


class Meta:
    db_table = 'Products'
    verbose_name = 'Продукт'
    verbose_name_plural = 'Продукты'
