from django.db import models
from equipment.models import Equipment
from django.urls import reverse
import uuid


class Rig(models.Model):

    STATUS_CHOICES = (
        ('working', 'Работает'),
        ('not_working', 'Не работает'),
        ('scheduled_maintenance', 'На плановом ремонте'),
        ('unknown', 'Статус неизвестен'),
    )

    name = models.CharField(max_length=150, verbose_name="Название буровой установки")
    uid = models.UUIDField(default=uuid.uuid4, editable=True, unique=True, verbose_name="Уникальный идентификатор")
    banner = models.ImageField(upload_to='rig_banners/', blank=True, verbose_name="Изображение буровой установки")
    equipments = models.ManyToManyField(Equipment, blank=True, verbose_name='Оборудование')
    description = models.TextField(blank=True, verbose_name="Описание буровой установки")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='not_working',
                              verbose_name='Состояние буровой установки')

    class Meta:
        # Порядок сортировки - по убыванию даты публикации
        ordering = ('name',)
        verbose_name = 'Буровую установку'
        verbose_name_plural = 'Буровые установки'

    def get_absolute_url(self):
        return reverse('rig:rig_detail', args=[self.uid])

    def __str__(self):
        return self.name
