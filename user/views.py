from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
# Create your views here.
from user.models import Employee

from user.serializers import EmployeeCreateSerializer, EmployeeSerializer


class EmployeeViewSet(viewsets.ViewSet):
    def get(self, request):
        employees = Employee.objects.all()

        if request.GET.get("username", None):
            employees = employees.filter(usuer_django_id__username__icontains=request.GET.get("username").lower())

        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def get_user(self, id):
        try:
            return Employee.objects.get(pk=id)
        except Employee.DoesnotExist:
            raise Http404

    def post(self, request):
        print(request.data)
        serializer = EmployeeCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, employee_id):
        employee = self.get_user(employee_id)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
