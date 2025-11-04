from django.test import TestCase
from django.contrib.auth.models import User
from .models import Note

class NoteModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.note = Note.objects.create(
            title='Test Note',
            content='This is a test note content.',
            owner=self.user
        )

    def test_note_creation(self):
        self.assertEqual(self.note.title, 'Test Note')
        self.assertEqual(self.note.content, 'This is a test note content.')
        self.assertEqual(self.note.owner.username, 'testuser')

    def test_note_created_at(self):
        self.assertIsNotNone(self.note.created_at)