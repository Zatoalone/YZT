# Generated by Django 3.2.15 on 2022-08-24 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rig', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rig',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание буровой установки'),
        ),
    ]