# Generated by Django 3.2 on 2021-04-25 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sedan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data_stor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.IntegerField(choices=[(1, 'Клиенты'), (2, 'Партнеры'), (3, 'Дистрибьюторы'), (4, 'Вендоры'), (5, 'Публичные домены'), (6, 'Отписавшиеся'), (6, 'Мусор')], verbose_name='Название таблицы')),
                ('file', models.FileField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]
