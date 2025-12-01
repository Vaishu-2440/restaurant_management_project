from rest_framework import serializers
from .models import ContactFormSubmission

class ContactFormSubmission(serializers.ModelSerializer) :
    class Meta :
        model = ContactFormSubmission
        fields = ['id', 'email', 'name', 'message', 'submitted_at']