# Generated by Django 3.2.15 on 2022-08-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название оборудования')),
                ('uid', models.CharField(max_length=150, verbose_name='Уникальный индетификатор')),
                ('banner', models.ImageField(blank=True, upload_to='blog_banners/', verbose_name='Изображение оборудования')),
                ('description', models.TextField(verbose_name='Описание оборудования')),
            ],
        ),
    ]
