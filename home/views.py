from rest_framework import generics
from .models import Table
from .serializers import TableListAPIView, TableDetailAPIView
from .serializers import TableSerializer
from rest_framework.generics import ListAPIView

class TableListAPIView(generics.ListAPIView) :
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    
class TableDetailAPIView(generics.RetrieveAPIView) :
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class AvailableTablesAPIView(ListAPIView) :
    serializer_class = TableSerializer
    
    def get_queryset(self) :
        return Table.objects.filter(is_available = True)

