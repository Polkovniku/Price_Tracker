# Price Tracker 🔍

Web service for monitoring product prices on the Rozetka marketplace.

Users add products they want to track by link or through search.
The service automatically checks prices once a day and stores the change history.
Each product page shows a price chart for the full tracking period.

## Deployment

The service is deployed on a VPS and available at https://pricetracker.pp.ua/. Swagger documentation is available at https://pricetracker.pp.ua//docs (user@gmail.com, userpassword)



---

## Tech Stack

**Backend**
- Python 3.12
- FastAPI
- SQLAlchemy (async) + asyncpg
- PostgreSQL
- Alembic
- Celery + Redis (Celery Beat for periodic jobs)
- Camoufox 
- JWT authentication (access + refresh tokens)
- Docker + Docker Compose

**Frontend**
- Vanilla HTML / CSS / JavaScript
- Nginx

---

## Features

- User registration and authentication
- Product search on Rozetka by name
- Add a product from a Rozetka link
- List of tracked products
- Product detail page with a price history chart
- Automatic daily price checks via Celery Beat
- Save price changes to history

---

## Run

### Requirements
- Docker
- Docker Compose

### 1. Clone the repository

```bash
git clone https://github.com/Polkovniku/Price_Tracker.git
cd Price_Tracker
```

### 2. Create a `.env` file in the backend directory

Set the variables:

```env
POSTGRES_DB=price_tracker_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
DB_HOST=db
DB_PORT=5432
SECRET_KEY=your_secret_key
```

Generate a `SECRET_KEY`:

```bash
openssl rand -hex 32
```

### 3. Start the app

```bash
docker compose up --build -d
```

### 4. Open in the browser

```
http://localhost
```

Swagger API docs: `http://localhost/docs`

---

## Project Structure

```
price_tracker/
├── backend/
│   ├── app/
│   │   ├── core/          # config, database, security
│   │   ├── models/        # SQLAlchemy models
│   │   ├── routers/       # FastAPI routers
│   │   ├── schemas/       # Pydantic schemas
│   │   ├── services/      # business logic + scraper
│   │   └── tasks/         # Celery tasks
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

## How It Works

1. The user adds a product by link or through search
2. The service parses data from Rozetka via Camoufox
3. The product is saved to the database with its initial price
4. Celery Beat checks current prices every 24 hours
5. When the price changes, the record is saved in `PriceHistory`
6. The user sees a price change chart on the product page

## Example

### Search by name or direct link

<img width="1919" height="910" alt="Снимок экрана 2026-08-17 160403" src="https://github.com/user-attachments/assets/d8a787fa-9e21-4fe6-b79e-5aca6dd51881" />

### View tracked products

<img width="1857" height="853" alt="Снимок экрана 2026-08-17 162514" src="https://github.com/user-attachments/assets/aae4202c-d0d7-4291-9f91-d884d9f64775" />

### Product details with price history

<img width="1897" height="908" alt="Снимок экрана 2026-08-17 162530" src="https://github.com/user-attachments/assets/9cb73f00-35c6-4fa2-87ba-147101ad922d" />


