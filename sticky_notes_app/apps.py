"""Module for apps."""
from django.apps import AppConfig


class StickyNotesAppConfig(AppConfig):
    """Class for app config."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "sticky_notes_app"
