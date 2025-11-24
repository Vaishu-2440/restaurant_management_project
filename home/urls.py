from django.urls import path, include
from .views import TableListAPIView, TableDetailAPIView

urlpatterns = [
    path('api/tables/', TableListAPIView.as_view(), name = 'table-list'),
    path('api/tables/<int : pk>/', TableDetailAPIView.as_view(), name = 'table-detail'),
]