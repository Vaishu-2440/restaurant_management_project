from django.urls import path, include
from .views import TableListAPIView, TableDetailAPIView
from .views import AvailableTablesAPIView

urlpatterns = [
    path('api/tables/', TableListAPIView.as_view(), name = 'table-list'),
    path('api/tables/<int:pk>/', TableDetailAPIView.as_view(), name = 'table-detail'),
    path('api/tables/available/', AvailableTablesAPIView.as_view(), name = 'available_tables_api'),
]