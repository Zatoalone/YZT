# Generated by Django 3.2.15 on 2022-08-31 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название месторождения')),
                ('uid', models.CharField(max_length=150, verbose_name='Уникальный месторождения')),
                ('description', models.TextField(blank=True, verbose_name='Описание месторождения')),
                ('geo', models.CharField(max_length=500, verbose_name='Координаты расположения')),
            ],
            options={
                'verbose_name': 'Месторождение',
                'verbose_name_plural': 'Месторождения',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='PurposeWell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название назначения')),
                ('description', models.TextField(blank=True, verbose_name='Описание назначения')),
            ],
            options={
                'verbose_name': 'Назначение',
                'verbose_name_plural': 'Назначения',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название формы')),
                ('description', models.TextField(blank=True, verbose_name='Описание формы')),
            ],
        ),
        migrations.CreateModel(
            name='StatusWell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название статуса')),
                ('description', models.TextField(blank=True, verbose_name='Описание статуса')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TypeWellbore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название типа')),
                ('description', models.TextField(blank=True, verbose_name='Описание типа')),
            ],
        ),
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название скважины')),
                ('uid', models.CharField(max_length=150, verbose_name='Уникальный идентификатор')),
                ('banner', models.ImageField(blank=True, upload_to='well_banners/', verbose_name='Изображение скважины')),
                ('nameLegal', models.CharField(max_length=150, verbose_name='Юридическое название скважины')),
                ('numLicense', models.CharField(max_length=150, verbose_name='Лицензионный номер скважины')),
                ('dTimLicense', models.DateField(verbose_name='Дата и время выдачи лицензии')),
                ('country', models.CharField(max_length=150, verbose_name='Страна, в которой находится скважина')),
                ('state', models.CharField(max_length=150, verbose_name='Штат или провинция, в которой находится скважина')),
                ('county', models.CharField(max_length=150, verbose_name='Район, в котором находится скважина')),
                ('region', models.CharField(max_length=150, verbose_name='Геополитический регион')),
                ('district', models.CharField(max_length=150, verbose_name='Название геополитического района')),
                ('block', models.CharField(max_length=150, verbose_name='Имя блока, в котором находится скважина')),
                ('timeZone', models.CharField(help_text='Это отклонение в часах и минутах от UTC. Это должен быть обычный часовой пояс на скважине, а не значение с учетом сезонных колебаний, такое как летнее время', max_length=150, verbose_name='Часовой пояс, в котором находится скважина')),
                ('operatorDiv', models.CharField(max_length=150, verbose_name='Подразделение операторской компании')),
                ('dTimSpud', models.DateField(verbose_name='Дата и время забуривания скважины')),
                ('dTimPa', models.DateField(verbose_name='Дата и время закрытия скважины')),
                ('wellheadElevation', models.CharField(max_length=150, verbose_name='Высота устья скважины относительно исходной точки')),
                ('groundElevation', models.CharField(help_text='Наземные буровые установки', max_length=150, verbose_name='Высота над уровнем земли')),
                ('waterDepth', models.CharField(help_text='Не наземные буровые установки', max_length=150, verbose_name='Глубина воды')),
                ('dTimCreation', models.DateField(auto_now_add=True, verbose_name='Дата и время создание объекта')),
                ('dTimLastChange', models.DateField(auto_now=True, verbose_name='Последнее изменение любого элемента данных')),
                ('description', models.TextField(blank=True, verbose_name='Комментарии и замечания')),
                ('field', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='well.field', verbose_name='Название месторождения, в котором находится скважина')),
                ('operator', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.company', verbose_name='Название компании-оператора')),
                ('purposeWell', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='well.purposewell', verbose_name='POSC назначение скважины')),
                ('statusWell', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='well.statuswell', verbose_name='POSC Состояние скважины')),
            ],
            options={
                'verbose_name': 'Скважину',
                'verbose_name_plural': 'Скважины',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Wellbore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название ствола скважины')),
                ('uid', models.CharField(max_length=150, verbose_name='Уникальный идентификатор')),
                ('number', models.CharField(blank=True, max_length=150, verbose_name='Номер скважины оператора')),
                ('numGovt', models.CharField(blank=True, max_length=150, verbose_name='Присвоенный правительством номер ствола скважины')),
                ('dTimKickoff', models.DateField(verbose_name='Дата и время запуска ствола скважины')),
                ('md', models.CharField(default='0', max_length=150, verbose_name='Измеренная глубина скважины. Если состояние «закупорено», указывает максимальную глубину, достигнутую до заглушки. Рекомендуется, чтобы это значение обновлялось примерно каждые 10 минут назначенным поставщиком необработанных данных на сайте')),
                ('tvd', models.CharField(default='0', max_length=150, verbose_name='Истинная вертикальная глубина скважины. Если состояние «закупорено», указывает максимальную глубину, достигнутую до заглушки. Рекомендуется, чтобы это значение обновлялось примерно каждые 10 минут назначенным поставщиком необработанных данных на сайте')),
                ('mdKickoff', models.CharField(default='0', max_length=150, verbose_name='Начальное измерение глубины ствола скважины')),
                ('tvdKickoff', models.CharField(default='0', max_length=150, verbose_name='Начальная истинная вертикальная глубина ствола скважины')),
                ('mdPlanned', models.CharField(default='0', max_length=150, verbose_name='Плановая измеренная глубина для общей глубины ствола скважины')),
                ('tvdPlanned', models.CharField(default='0', max_length=150, verbose_name='Плановая истинная глубина по вертикали для общей глубины ствола скважины')),
                ('mdSubSeaPlanned', models.CharField(blank=True, max_length=150, verbose_name='Плановое измерение общей глубины ствола скважины - по отношению к морскому дну')),
                ('tvdSubSeaPlanned', models.CharField(blank=True, max_length=150, verbose_name='Плановая истинная глубина по вертикали при общей глубине ствола скважины относительно морского дна')),
                ('dayTarget', models.IntegerField(default=1, verbose_name='Расчетные дни для бурения ствола скважины')),
                ('dTimLastChange', models.DateField(auto_now=True, verbose_name='Последнее изменение любого элемента данных')),
                ('description', models.TextField(blank=True, verbose_name='Комментарии и замечания')),
                ('nameWell', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='well.well', verbose_name='Название скважины')),
                ('purposeWellbore', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='well.purposewell', verbose_name='POSC назначение ствола скважины')),
                ('shape', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='well.shape', verbose_name='POSC форма траектории ствола скважины')),
                ('statusWellbore', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='well.statuswell', verbose_name='POSC состояние ствола скважины')),
                ('typeWellbore', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='well.typewellbore', verbose_name='Тип ствола скважины')),
            ],
            options={
                'verbose_name': 'Ствол скважины',
                'verbose_name_plural': 'Стволы скважин',
                'ordering': ('name',),
            },
        ),
    ]
