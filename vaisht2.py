# Serializer for the Note model.
# Converts Note instances to JSON and ensures the 'owner' field is read-only.

from rest_framework import serializers
from myapp.models import Note  # 👈 Use your actual app name here

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'owner']
        read_only_fields = ['owner']
