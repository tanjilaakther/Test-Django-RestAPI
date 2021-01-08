from django.db import models

# Create your models here.
class EmployeeInfo(models.Model):
    employeeName = models.CharField(max_length=200)
    employeeID = models.CharField(max_length=200)
    employeeAge = models.CharField(max_length=200)
    employeeDesignation = models.CharField(max_length=200)

    def __str__(self):
        return self.employeeName
    