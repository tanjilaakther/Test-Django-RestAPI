from django.shortcuts import render

from rest_framework import viewsets
from .serializers import EmployeeInfoSerializer
from .models import EmployeeInfo
# Create your views here.

class EmployeeInfoViewSet(viewsets.ModelViewSet):
    queryset = EmployeeInfo.objects.all().order_by('employeeID')
    serializer_class = EmployeeInfoSerializer
