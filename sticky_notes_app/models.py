#type: ignore
"""Module for models."""
from django.db import models

class Note(models.Model):
    """
    A model representing a sticky note.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self) -> str:
        """
        String representation of the Note object.
        """
        return str(self.title)
