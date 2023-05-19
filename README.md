## Платформа торговой сети электроники Market

В данном проекте представлено веб-приложение для работы торговой сети электроники с поставщиками и продавцами, 
с API интерфейсом и админ-панелью.

### Стек:
- python 3.11.3
- Django 4.2.1
- PostgreSQL 12.4-alpine
- DRF 3.14.0

___
Для запуска проекта на локальной машине следует выполнить в терминале следующие команды:
```
docker-compose up -d
python manage.py migrate

```
Для создания админа нужно выполнить команду:
```
python manage.py createsuperuser

```