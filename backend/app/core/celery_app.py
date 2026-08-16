from celery import Celery
from app.core.config import settings

celery_app = Celery("price_tracker", broker=settings.redis_url, backend=settings.redis_url, include=["app.tasks.celery_tasks"])

celery_app.conf.beat_schedule = {
    "check-prices": {
        "task": "app.tasks.celery_tasks.check_prices",
        "schedule": 86400.0,
    }
}