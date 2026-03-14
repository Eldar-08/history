# Мой сайт по истории

Django-приложение для изучения исторических фактов с регистрацией пользователей.

## Локальный запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/yourrepo.git
   cd history_site
   ```

2. Создайте виртуальное окружение:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Создайте .env файл на основе .env.example:
   ```bash
   cp .env.example .env
   # Отредактируйте .env с вашими настройками
   ```

5. Примените миграции:
   ```bash
   python manage.py migrate
   ```

6. Создайте суперпользователя:
   ```bash
   python manage.py createsuperuser
   ```

7. Запустите сервер:
   ```bash
   python manage.py runserver
   ```

Откройте http://127.0.0.1:8000/

## Развертывание

### Railway (рекомендуется для новичков)

1. Зарегистрируйтесь на [Railway.app](https://railway.app)
2. Подключите GitHub-репозиторий
3. Добавьте переменные окружения из .env
4. Railway автоматически развернёт приложение

### Heroku

1. Установите Heroku CLI
2. Создайте приложение:
   ```bash
   heroku create your-app-name
   ```
3. Добавьте переменные окружения:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   # и т.д.
   ```
4. Разверните:
   ```bash
   git push heroku main
   ```

### VPS (Ubuntu + Nginx + Gunicorn)

1. Установите сервер
2. Клонируйте код
3. Установите зависимости
4. Настройте PostgreSQL
5. Настройте Nginx и Gunicorn
6. Получите SSL-сертификат (Let's Encrypt)

## Функции

- Регистрация и авторизация пользователей
- Красивая HTML-страница с шаблонами
- База данных для хранения пользователей
- Готово к монетизации (добавьте платежи, премиум-контент и т.д.)

## Структура проекта

```
history_site/
├── config/          # Django settings
├── core/            # Основное приложение
├── static/          # Статические файлы
├── templates/       # Шаблоны
├── requirements.txt # Зависимости
├── Procfile         # Для Heroku/Railway
└── .env.example     # Пример переменных окружения
```