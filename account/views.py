from rest_framework.viewsets import ModelViewSet
from models import Staff
from .serializers import StaffSerializer

class StaffViewSet(ModelViewSet) :
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer



"""
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserProfileUpdateSerializer

class UserProfileUpdateAPIView(APIView) :
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request) :
        user = request.user
        serializer = UserProfileUpdateSerilaizer(
            user, data = request.data, partial = True
        )
        if serializer.is_valid() :
            serializer.save()
            return Response(
                {"message" : "Profile updated successfully.", "data" : serializer.data},
                status = status.HTTP_200_OK
            )
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 
"""
