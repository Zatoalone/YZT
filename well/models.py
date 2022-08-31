from django.db import models
from django.urls import reverse
from core.models import Company
import uuid


class Field(models.Model):
    """
        Месторождения
    """
    name = models.CharField(max_length=150, verbose_name="Название месторождения")
    uid = models.UUIDField(default=uuid.uuid4, editable=True, unique=True, verbose_name="Уникальный идентификатор")
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
    uid = models.UUIDField(default=uuid.uuid4, editable=True, unique=True, verbose_name="Уникальный идентификатор")
    banner = models.ImageField(upload_to='well_banners/', blank=True, verbose_name="Изображение скважины")
    nameLegal = models.CharField(max_length=150, verbose_name="Юридическое название скважины")
    numLicense = models.CharField(max_length=150, verbose_name="Лицензионный номер скважины")
    dTimLicense = models.DateField(verbose_name='Дата и время выдачи лицензии')
    field = models.ForeignKey(Field, on_delete=models.CASCADE,
                                 verbose_name='Название месторождения, в котором находится скважина')
    country = models.CharField(max_length=150, verbose_name="Страна, в которой находится скважина")
    state = models.CharField(max_length=150, verbose_name="Штат или провинция, в которой находится скважина")
    county = models.CharField(max_length=150, verbose_name="Район, в котором находится скважина")
    region = models.CharField(max_length=150, verbose_name="Геополитический регион")
    district = models.CharField(max_length=150, verbose_name="Название геополитического района")
    block = models.CharField(max_length=150, verbose_name="Имя блока, в котором находится скважина")
    timeZone = models.CharField(max_length=150, verbose_name="Часовой пояс, в котором находится скважина",
                                help_text="Это отклонение в часах и минутах от UTC. Это должен быть обычный часовой пояс на скважине, а не значение с учетом сезонных колебаний, такое как летнее время")
    operator = models.ForeignKey(Company, on_delete=models.CASCADE,
                                 verbose_name='Название компании-оператора')
    operatorDiv = models.CharField(max_length=150, verbose_name="Подразделение операторской компании")
    statusWell = models.ForeignKey(StatusWell, on_delete=models.CASCADE, verbose_name='POSC Состояние скважины')
    purposeWell = models.ForeignKey(PurposeWell, on_delete=models.CASCADE, verbose_name='POSC назначение скважины')
    dTimSpud = models.DateField(verbose_name='Дата и время забуривания скважины')
    dTimPa = models.DateField(verbose_name='Дата и время закрытия скважины')
    wellheadElevation = models.CharField(max_length=150,
                                         verbose_name="Высота устья скважины относительно исходной точки")
    groundElevation = models.CharField(max_length=150, verbose_name="Высота над уровнем земли",
                                       help_text="Наземные буровые установки")
    waterDepth = models.CharField(max_length=150, verbose_name="Глубина воды",
                                  help_text="Не наземные буровые установки")

    dTimCreation = models.DateField(auto_now_add=True, verbose_name='Дата и время создание объекта')
    dTimLastChange = models.DateField(auto_now=True, verbose_name='Последнее изменение любого элемента данных')

    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        # Порядок сортировки - по убыванию даты публикации
        ordering = ('name',)
        verbose_name = 'Скважину'
        verbose_name_plural = 'Скважины'

    def get_absolute_url(self):
        return reverse('well:well_detail', args=[self.uid])

    def __str__(self):
        return self.name


class TypeWellbore(models.Model):
    """
        Типы ствола скважины
    """
    name = models.CharField(max_length=150, verbose_name="Название типа")
    description = models.TextField(blank=True, verbose_name="Описание типа")

    class Meta:
        # Порядок сортировки - по убыванию даты публикации
        ordering = ('name',)
        verbose_name = 'Тип ствола'
        verbose_name_plural = 'Типы стволов'

    def __str__(self):
        return self.name


class Shape(models.Model):
    """
        Формы траектории стволов скважины
    """
    name = models.CharField(max_length=150, verbose_name="Название формы")
    description = models.TextField(blank=True, verbose_name="Описание формы")

    class Meta:
        # Порядок сортировки - по убыванию даты публикации
        ordering = ('name',)
        verbose_name = 'Форму траектории'
        verbose_name_plural = 'Формы траектории'

    def __str__(self):
        return self.name


class Wellbore(models.Model):
    """
        Стволы скважин
    """
    name = models.CharField(max_length=150, verbose_name="Название ствола скважины")
    uid = models.UUIDField(default=uuid.uuid4, editable=True, unique=True, verbose_name="Уникальный идентификатор")
    nameWell = models.ForeignKey(Well, on_delete=models.CASCADE, verbose_name='Название скважины')
    number = models.CharField(max_length=150, verbose_name="Номер скважины оператора", blank=True,)
    numGovt = models.CharField(max_length=150, verbose_name="Присвоенный правительством номер ствола скважины", blank=True,)
    statusWellbore = models.ForeignKey(StatusWell, on_delete=models.CASCADE,
                                          verbose_name='POSC состояние ствола скважины',default=1)
    purposeWellbore = models.ForeignKey(PurposeWell, on_delete=models.CASCADE,
                                           verbose_name='POSC назначение ствола скважины', default=1)
    typeWellbore = models.ForeignKey(TypeWellbore, on_delete=models.CASCADE, verbose_name='Тип ствола скважины')
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE, verbose_name="POSC форма траектории ствола скважины")
    dTimKickoff = models.DateTimeField(verbose_name='Дата и время запуска ствола скважины',)
    md = models.CharField(max_length=150, default="0",
                          verbose_name="Измеренная глубина скважины. Если состояние «закупорено», "
                                       "указывает максимальную глубину, достигнутую до заглушки. "
                                       "Рекомендуется, чтобы это значение обновлялось примерно каждые 10 минут "
                                       "назначенным поставщиком необработанных данных на сайте")
    tvd = models.CharField(max_length=150, default="0",
                           verbose_name="Истинная вертикальная глубина скважины. Если состояние «закупорено», указывает"
                                        " максимальную глубину, достигнутую до заглушки. Рекомендуется, чтобы это "
                                        "значение обновлялось примерно каждые 10 минут назначенным поставщиком "
                                        "необработанных данных на сайте")
    mdKickoff = models.CharField(max_length=150, default="0", verbose_name="Начальное измерение глубины ствола "
                                                                           "скважины")
    tvdKickoff = models.CharField(max_length=150, default="0", verbose_name="Начальная истинная вертикальная глубина "
                                                                            "ствола скважины")
    mdPlanned = models.CharField(max_length=150, default="0", verbose_name="Плановая измеренная глубина для общей "
                                                                           "глубины ствола скважины")
    tvdPlanned = models.CharField(max_length=150, default="0", verbose_name="Плановая истинная глубина по вертикали для"
                                                                            " общей глубины ствола скважины")
    mdSubSeaPlanned = models.CharField(max_length=150, blank=True,
                                       verbose_name="Плановое измерение общей глубины ствола скважины - по отношению к "
                                                    "морскому дну")
    tvdSubSeaPlanned = models.CharField(max_length=150, blank=True,
                                        verbose_name="Плановая истинная глубина по вертикали при общей глубине ствола "
                                                     "скважины относительно морского дна")
    dayTarget = models.IntegerField(default=1, verbose_name="Расчетные дни для бурения ствола скважины")
    dTimCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создание объекта')
    dTimLastChange = models.DateTimeField(auto_now=True, verbose_name='Последнее изменение любого элемента данных')
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        # Порядок сортировки - по убыванию даты публикации
        ordering = ('name',)
        verbose_name = 'Ствол скважины'
        verbose_name_plural = 'Стволы скважин'

    def get_absolute_url(self):
        return reverse('wellbore:wellbore_detail', args=[self.uid])

    def __str__(self):
        return self.name
