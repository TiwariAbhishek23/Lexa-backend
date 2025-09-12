from fastapi import FastAPI
from app.core.settings import settings
from app.routes import fixed, ask


def include_router(app):
    app.include_router(fixed.router)
    app.include_router(ask.router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    return app

app = start_application()