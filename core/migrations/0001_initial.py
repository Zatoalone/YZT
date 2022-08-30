# Generated by Django 3.2.15 on 2022-08-22 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=150, verbose_name='Полное название организации')),
                ('short_name', models.CharField(blank=True, max_length=250, verbose_name='Сокращенное название организации')),
                ('ogrn', models.CharField(blank=True, max_length=40, verbose_name='ОГРН')),
                ('grn', models.CharField(blank=True, max_length=40, verbose_name='ГРН')),
                ('address_le', models.CharField(blank=True, max_length=150, verbose_name='Адрес юридического лица ')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('created', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('reliable', 'Надежый'), ('indefined', 'Статус неопределен'), ('unreliable', 'Ненадежный')], default='indefined', max_length=10)),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
                'ordering': ('short_name',),
            },
        ),
    ]