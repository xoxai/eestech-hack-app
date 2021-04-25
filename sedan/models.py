from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class TestClass(models.Model):
    test_int = models.IntegerField()
    test_int2 = models.IntegerField()

class Data_stor(models.Model):
    table_names = (
        (1, 'Клиенты'),
        (2, 'Партнеры'),
        (3, 'Дистрибьюторы'),
        (4, 'Вендоры'),
        (5, 'Публичные домены'),
        (6, 'Отписавшиеся'),
        (7, 'Мусор'),
    )
    table_name = models.IntegerField(verbose_name='Название таблицы', choices= table_names)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    file = models.FileField()

