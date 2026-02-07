Структура:
movie_service/
├── alembic/              # Миграции базы данных
├── src/                  # Исходный код приложения
│   ├── main.py           # Точка входа (создание FastAPI app)
│   ├── config.py         # Настройки (pydantic-settings, ENV переменные)
│   ├── database.py       # Подключение к БД и сессии (SQLAlchemy/Tortoise)
│   ├── dependencies.py   # Общие зависимости (get_db, текущий юзер)
│   │
│   ├── auth/             # Модуль аутентификации (если будет)
│   │
│   ├── movies/           # Модуль фильмов (основной домен)
│   │   ├── router.py     # API эндпоинты (GET /movies, POST /movies)
│   │   ├── schemas.py    # Pydantic модели (валидация входящих/исходящих данных)
│   │   ├── models.py     # SQLAlchemy модели (таблицы в БД)
│   │   ├── service.py    # Бизнес-логика (CRUD операции, сложные фильтры)
│   │   ├── constants.py  # Специфичные константы модуля
│   │   └── dependencies.py # Зависимости только для этого модуля
│   │
│   ├── users/            # Модуль пользователей
│   │   └── ...           # (структура аналогична movies)
│   │
│   └── common/           # Общие утилиты, базовые классы, кастомные ошибки
│
├── tests/                # Тесты (pytest)
├── .env                  # Секреты (не пушить в git!)
├── alembic.ini           # Конфиг алембика
├── docker-compose.yaml   # Запуск БД, Redis и приложения
└── pyproject.toml        # Зависимости (poetry/pip)

"poetry add название_библиотеки" - для добавления библиотеки