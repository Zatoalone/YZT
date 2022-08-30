# YZT

MVP приложение для IT-чемпионата нефтяной отрасли

## Установка
### Подготовка
* Подготовка виртуального окружения **python3 -m venv web-dev_oil**
* Активация виртуального окружения **source web-dev_oil/bin/activate** (деактивация **deactivate**)
* Клонирование проекта **git clone https://github.com/Zatoalone/YZT.git**
* Установка зависимостей **cd /YZT** **pip install -r requarements.txt**
* Выполнение миграций **python manage.py migrate**
* Создание администратора системы **python manage.py createsuperuser**

### Запуск
* Запуск встроенного сервера **python manage.py runserver**