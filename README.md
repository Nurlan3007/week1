# Докеризированное Python-приложение с PostgreSQL

Этот проект разворачивает веб-приложение на Python с использованием Flask и PostgreSQL в Docker.

## Предварительные требования
- Docker
- Docker Compose

## Структура проекта
```
.
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── init.sql (если нужен для инициализации БД)
└── app (файлы вашего Python-приложения)
```

## Установка и запуск
### 1. Сборка и запуск контейнеров
```sh
docker-compose up --build
```

### 2. Остановка контейнеров
```sh
docker-compose down
```

## Сервисы
### База данных (PostgreSQL)
- Образ: `postgres:13`
- Работает на порту `5438`
- Переменные окружения:
  - `POSTGRES_USER=postgres`
  - `POSTGRES_PASSWORD=root`
  - `POSTGRES_DB=week1`
- Монтирует `init.sql` для инициализации БД (опционально)

### Веб-приложение
- Собирается из `Dockerfile`
- Работает на порту `5000`
- Использует Flask
- Подключается к PostgreSQL через переменные окружения:
  - `DB_HOST=db`
  - `DB_NAME=week1`
  - `DB_USER=postgres`
  - `DB_PASSWORD=root`
- Запускает `test.py` как основной скрипт

## Зависимости
Указаны в `requirements.txt`:
```
psycopg2
flask
```

## Примечания
- Убедитесь, что `test.py` находится в корневой директории и правильно настроен для использования Flask.
- В продакшене учетные данные базы данных должны быть защищены.
- При необходимости измените `docker-compose.yml` для дополнительной конфигурации.

## Лицензия
MIT License (или укажите вашу лицензию).
