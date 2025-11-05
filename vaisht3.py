# ViewSet for the Note model.
# Provides create, retrieve, update, and delete actions.
# Automatically assigns the logged-in user as the note owner.

from rest_framework import viewsets, permissions
from myapp.models import Note  # Replace 'myapp' with your actual app name
from myapp.serializers import NoteSerializer  # Import your serializer

class NoteViewSet(viewsets.ModelViewSet):
    """API endpoint for managing user notes."""
    
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Return only the notes belonging to the logged-in user."""
        return Note.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """Assign the currently logged-in user as the note owner."""
        serializer.save(owner=self.request.user)
