from rest_framework import serializers
from .models import EmployeeInfo

class EmployeeInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmployeeInfo
        fields = ('id','employeeName', 'employeeID', 'employeeAge', 'employeeDesignation')