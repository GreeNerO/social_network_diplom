# Дипломная работа профессии «Python-разработчик с нуля»

## Описание проекта
Социальная сеть, разработанная на Django с использованием Django REST Framework.

## Требования
- Python 3.8+
- PostgreSQL
- pip (менеджер пакетов Python)

## Установка и запуск проекта

1. Клонируйте репозиторий:
```bash
git clone <url-репозитория>
cd social_network
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Примените миграции:
```bash
python manage.py migrate
```

4. Создайте суперпользователя (опционально):
```bash
python manage.py createsuperuser
```

6. Создайте файл `.env` в корневой директории проекта и добавьте следующие переменные окружения:
DEBUG=
SECRET_KEY=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

5. Запустите сервер разработки:
```bash
python manage.py runserver
```

После запуска сервера, приложение будет доступно по адресу http://127.0.0.1:8000/

## Тестирование
Для запуска тестов используйте команду:
```bash
pytest
```

## Структура проекта
- `social_network/` - основной пакет Django проекта
- `posts/` - приложение для работы с постами
- `media/` - директория для загруженных файлов
- `manage.py` - скрипт управления Django проектом
- `requirements.txt` - список зависимостей проекта



