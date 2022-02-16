import os

DJANGO_DATABASE_BACKEND = os.environ.get("DJANGO_DATABASE_BACKEND", "sqlite")
if DJANGO_DATABASE_BACKEND == "postgres":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "CONN_MAX_AGE": 290,
            "NAME": os.environ.get("WEDDING_DB"),
            "USER": os.environ.get("POSTGRES_NONROOT_USER"),
            "PASSWORD": os.environ.get("POSTGRES_NONROOT_PASSWORD"),
            "HOST": "postgres",
            "PORT": 5432,
        }
    }
else:
    DATABASES = None


SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

DEBUG = not os.environ.get("DJANGO_DEBUG") in ["FALSE", "false", "False"]

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOST")


# This is used in a few places where the names of the couple are used
BRIDE_AND_GROOM = os.environ.get("BRIDE_AND_GROOM")
# base address for all emails
DEFAULT_WEDDING_EMAIL = os.environ.get("WEDDING_EMAIL")
# website
# the location of your wedding
WEDDING_LOCATION = os.environ.get("WEDDING_LOCATION")
# the date of your wedding
WEDDING_DATE = os.environ.get("WEDDING_DATE")

WEDDING_WEBSITE_URL = os.environ.get("WEDDING_WEBSITE_URL")


STATIC_ROOT = os.environ.get("PROJECT_STATIC")
