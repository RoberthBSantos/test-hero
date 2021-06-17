from django.http import Http404
from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from company.serializers import CompanySerializer, CompanyCreateSerializer
from company.models import Company


# Create your views here.

class CompanyViewSet(viewsets.ViewSet):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def get_company(self, id):
        try:
            return Company.objects.get(pk=id)
        except Company.DoesNotExist:
            raise Http404

    def show(self, request, id):
        company = self.get_company(id)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanyCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, company_id):
        company = self.get_company(company_id)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
