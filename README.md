# Price Tracker 🔍

Веб-сервіс для моніторингу цін на товари з маркетплейсу Rozetka.

Користувач додає товари, які хоче відстежувати - за посиланням або через пошук.
Сервіс автоматично перевіряє ціни раз на добу та зберігає історію змін.
На сторінці кожного товару відображається графік зміни ціни за весь час відстеження.

## Деплой

Сервіс розмещенний на VPS та доступний за посиланням https://pricetracker.pp.ua/ , також  документація Swagger за https://pricetracker.pp.ua//docs

---

## Стек технологій

**Backend**
- Python 3.12
- FastAPI
- SQLAlchemy (async) + asyncpg
- PostgreSQL
- Alembic
- Celery + Redis (Celery Beat для періодичних задач)
- Camoufox 
- JWT аутентификация (access + refresh токени)
- Docker + Docker Compose

**Frontend**
- Vanilla HTML / CSS / JavaScript
- Nginx

---

## Функціональність

- Реєстрація та авторизація користувачів
- Пошук товарів на Rozetka за назвою
- Додавання товару за посиланням з Rozetka
- Список товарів, що відстежуються
- Детальна сторінка товару з графіком історії цін
- Автоматична перевірка цін щодня через Celery Beat
- При зміні ціни – збереження в історію

---

## Запуск

### Вимоги
- Docker
- Docker Compose

### 1. Клонувати репозиторій

```bash
git clone https://github.com/Polkovniku/Price_Tracker.git
cd Price_Tracker
```

### 2. Створити `.env` файл в backend директорії

Заповнити змінні:

```env
POSTGRES_DB=price_tracker_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
DB_HOST=db
DB_PORT=5432
SECRET_KEY=your_secret_key
```

Згенерувати `SECRET_KEY`:

```bash
openssl rand -hex 32
```

### 3. Запустити

```bash
docker compose up --build -d
```

### 4. Відкрити у браузері

```
http://localhost
```

API документація Swagger: `http://localhost/docs`

---

## Структура проекту

```
price_tracker/
├── backend/
│   ├── app/
│   │   ├── core/          # config, database, security
│   │   ├── models/        # SQLAlchemy моделі
│   │   ├── routers/       # FastAPI роутери
│   │   ├── schemas/       # Pydantic схеми
│   │   ├── services/      # бізнес-логіка + scraper
│   │   └── tasks/         # Celery таски
│   ├── alembic/
│   ├── Dockerfile
│   └── pyproject.toml
├── frontend/
│   ├── css/
│   ├── js/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── search.html
│   ├── tracked.html
│   └── product.html
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
└── docker-compose.yml
```

---

## Як це працює

1. Користувач додає товар за посиланням або через пошук
2. Сервіс парсить дані з Розетки через Camoufox
3. Товар зберігається у БД із початковою ціною
4. Celery Beat кожні 24 години перевіряє актуальні ціни
5. При зміні ціни - запис зберігається в `PriceHistory`
6. Користувач бачить графік зміни цін на сторінці товару

## Приклад роботи

### Пошук товару

<img width="1919" height="910" alt="Снимок экрана 2026-08-17 160403" src="https://github.com/user-attachments/assets/d8a787fa-9e21-4fe6-b79e-5aca6dd51881" />

### Перегляд відстежуваних товарів

<img width="1857" height="853" alt="Снимок экрана 2026-08-17 162514" src="https://github.com/user-attachments/assets/aae4202c-d0d7-4291-9f91-d884d9f64775" />

### Детальна інформація з исторією цін

<img width="1897" height="908" alt="Снимок экрана 2026-08-17 162530" src="https://github.com/user-attachments/assets/9cb73f00-35c6-4fa2-87ba-147101ad922d" />



