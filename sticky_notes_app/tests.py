#type: ignore
"""Module for Test"""
from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteModelTest(TestCase):
    """Class representing test"""
    def setUp(self):
        self.note = Note.objects.create(title="Test Note", content="This is a test note.")

    def test_note_creation(self):
        """
        Test that a Note instance can be created and saved.
        """
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(self.note.content, "This is a test note.")
        self.assertTrue(isinstance(self.note, Note))
        self.assertEqual(str(self.note), self.note.title)

class NoteViewTest(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title="Test Note", content="This is a test note.")

    def test_note_list_view(self):
        """
        Test that the note list view returns a 200 status code and uses the correct template.
        """
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sticky_notes_app/note_list.html')
        self.assertContains(response, self.note.title)

    def test_note_detail_view(self):
        """
        Test that the note detail view returns a 200 status code and uses the correct template.
        """
        response = self.client.get(reverse('note_detail', args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sticky_notes_app/note_detail.html')
        self.assertContains(response, self.note.title)
        self.assertContains(response, self.note.content)

    def test_note_create_view(self):
        """
        Test that the note create view can create a new note.
        """
        response = self.client.post(reverse('note_new'), {
            'title': 'New Note',
            'content': 'This is a new note.'
        })
        self.assertEqual(response.status_code, 302)
        new_note = Note.objects.get(title='New Note')
        self.assertEqual(new_note.content, 'This is a new note.')

    def test_note_update_view(self):
        """
        Test that the note update view can update an existing note.
        """
        response = self.client.post(reverse('note_edit', args=[self.note.pk]), {
            'title': 'Updated Note',
            'content': 'This is an updated note.'
        })
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')
        self.assertEqual(self.note.content, 'This is an updated note.')

    def test_note_delete_view(self):
        """
        Test that the note delete view can delete an existing note.
        """
        response = self.client.post(reverse('note_delete', args=[self.note.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
