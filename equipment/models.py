from django.db import models
from django.urls import reverse
import uuid


class Equipment(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название оборудования")
    uid = models.UUIDField(default=uuid.uuid4, editable=True, unique=True, verbose_name="Уникальный идентификатор")
    banner = models.ImageField(upload_to='equipment_banners/', blank=True, verbose_name="Изображение оборудования")
    description = models.TextField(blank=True, verbose_name="Описание оборудования")

    class Meta:
        # Порядок сортировки - по убыванию даты публикации
        ordering = ('name',)
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'

    def get_absolute_url(self):
        return reverse('equipment:equipment_detail', args=[self.uid])

    def __str__(self):
        return self.name
