"""Shared paths and settings for local dev and WSGI hosts (e.g. PythonAnywhere)."""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

USERS_DB = os.path.join(BASE_DIR, "users.db")
STOCKS_DB = os.path.join(BASE_DIR, "stocks.db")
PORTFOLIO_DB = os.path.join(BASE_DIR, "portfolio.db")

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf",
)
DEBUG = os.environ.get("FLASK_DEBUG", "").lower() in ("1", "true", "yes")
