from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='reliable')


class Company(models.Model):
    """
        Компании
    """

    STATUS_CHOICES = (
        ('reliable', 'Надежый'),
        ('indefined', 'Статус неопределен'),
        ('unreliable', 'Ненадежный'),
    )

    full_name = models.CharField(max_length=150, blank=True, verbose_name="Полное название организации")
    short_name = models.CharField(max_length=250, blank=True, verbose_name="Сокращенное название организации")
    ogrn = models.CharField(max_length=40, blank=True, verbose_name="ОГРН")
    grn = models.CharField(max_length=40, blank=True, verbose_name="ГРН")
    address_le = models.CharField(max_length=150, blank=True, verbose_name="Адрес юридического лица ")
    description = models.TextField(blank=True, verbose_name="Описание")
    # Поле для даты заведения организации
    created = models.DateField(auto_now_add=True)
    # Поле для даты изменения организации
    update = models.DateField(auto_now=True)
    # Поле для отображения состояния организации (опубликовано/черновик)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='indefined', verbose_name="Статус")

    # Метаданные
    class Meta:
        # Порядок сортировки - по убыванию даты публикации
        ordering = ('short_name',)
        verbose_name = 'Компанию'
        verbose_name_plural = 'Компании'

    objects = models.Manager()
    published = PublishedManager()


    # Метод, отвечающий за отображение объекта в человекочитаемом формате

    def __str__(self):
        return self.short_name
