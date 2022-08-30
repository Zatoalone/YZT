from django.db import models
from django.urls import reverse
from core.models import Company


class Field(models.Model):
    """
        Месторождения
    """
    name = models.CharField(max_length=150, verbose_name="Название месторождения")
    uid = models.CharField(max_length=150, verbose_name="Уникальный месторождения")
    description = models.TextField(blank=True, verbose_name="Описание месторождения")
    geo = models.CharField(max_length=500, verbose_name="Координаты расположения")

    class Meta:
        # Порядок сортировки - по убыванию даты публикации
        ordering = ('name',)
        verbose_name = 'Месторождение'
        verbose_name_plural = 'Месторождения'

    def __str__(self):
        return self.name


class StatusWell(models.Model):
    """
        Статус скважины
    """
    name = models.CharField(max_length=150, verbose_name="Название статуса")
    description = models.TextField(blank=True, verbose_name="Описание статуса")

    class Meta:
        # Порядок сортировки - по убыванию даты публикации
        ordering = ('name',)
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


class PurposeWell(models.Model):
    """
           Назначение скважины
    """
    name = models.CharField(max_length=150, verbose_name="Название назначения")
    description = models.TextField(blank=True, verbose_name="Описание назначения")

    class Meta:
        # Порядок сортировки - по убыванию даты публикации
        ordering = ('name',)
        verbose_name = 'Назначение'
        verbose_name_plural = 'Назначения'

    def __str__(self):
        return self.name


class Well(models.Model):
    """
        Скважина
    """
    name = models.CharField(max_length=150, verbose_name="Название скважины")
    uid = models.CharField(max_length=150, verbose_name="Уникальный идентификатор")
    nameLegal = models.CharField(max_length=150, verbose_name="Юридическое название скважины")
    numLicense = models.CharField(max_length=150, verbose_name="Лицензионный номер скважины")
    dTimLicense = models.DateField(verbose_name='Дата и время выдачи лицензии')
    field = models.OneToOneField(Field, on_delete=models.CASCADE,
                                 verbose_name='Название месторождения, в котором находится скважина')
    country = models.CharField(max_length=150, verbose_name="Страна, в которой находится скважина")
    state = models.CharField(max_length=150, verbose_name="Штат или провинция, в которой находится скважина")
    county = models.CharField(max_length=150, verbose_name="Район, в котором находится скважина")
    region = models.CharField(max_length=150, verbose_name="Геополитический регион")
    district = models.CharField(max_length=150, verbose_name="Название геополитического района")
    block = models.CharField(max_length=150, verbose_name="Имя блока, в котором находится скважина")
    timeZone = models.CharField(max_length=150, verbose_name="Часовой пояс, в котором находится скважина",
                                help_text="Это отклонение в часах и минутах от UTC. Это должен быть обычный часовой пояс на скважине, а не значение с учетом сезонных колебаний, такое как летнее время")
    operator = models.OneToOneField(Company, on_delete=models.CASCADE,
                                 verbose_name='Название компании-оператора')
    operatorDiv = models.CharField(max_length=150, verbose_name="Подразделение операторской компании")
    statusWell = models.OneToOneField(StatusWell, on_delete=models.CASCADE, verbose_name='POSC Состояние скважины')
    purposeWell = models.OneToOneField(PurposeWell, on_delete=models.CASCADE, verbose_name='POSC назначение скважины')
    dTimSpud = models.DateField(verbose_name='Дата и время забуривания скважины')
    dTimPa = models.DateField(verbose_name='Дата и время закрытия скважины')
    wellheadElevation = models.CharField(max_length=150,
                                         verbose_name="Высота устья скважины относительно исходной точки")
    groundElevation = models.CharField(max_length=150, verbose_name="Высота над уровнем земли",
                                       help_text="Наземные буровые установки")
    waterDepth = models.CharField(max_length=150, verbose_name="Глубина воды",
                                  help_text="Не наземные буровые установки")

    dTimCreation = models.DateField(auto_now_add=True, verbose_name='Дата и время забуривания скважины')
    dTimLastChange = models.DateField(auto_now=True, verbose_name='Последнее изменение любого элемента данных')

    comments = models.TextField(blank=True, verbose_name="Комментарии и замечания")

    class Meta:
        # Порядок сортировки - по убыванию даты публикации
        ordering = ('name',)
        verbose_name = 'Скважину'
        verbose_name_plural = 'Скважины'

    def get_absolute_url(self):
        return reverse('well:well_detail', args=[self.uid])

    def __str__(self):
        return self.name
