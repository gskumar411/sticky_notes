#type: ignore
"""Module for Forms."""
from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    """
    A form for creating and updating Note instances.
    """
    class Meta:
        """Class for fields."""
        model = Note
        fields = ['title', 'content']
