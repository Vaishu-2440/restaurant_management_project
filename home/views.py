from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import ContactFormSubmission
from .serializers import ContactFormSubmissionSerializer

class ContactFormSubmissionView(CreateAPIView) :
    queryset = ContactFormSubmission.objects.all()
    serializer_class = ContactFormSubmissionSerializer

    def create(self, request, *args, **kwargs) :
        serializer = self.get_serializer(data = request.data)
        if serialzier.is_valid() :
            serialzier.save()
            return Response(
                {"message" : "Contact Form submitted successfully", "data" : serializer.data },
                status = status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

