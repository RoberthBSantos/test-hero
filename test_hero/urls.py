"""test_hero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from company.views import CompanyViewSet
from user.views import EmployeeViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/', CompanyViewSet.as_view({"post": "post"})),
    path('company/', CompanyViewSet.as_view({"get": "get"})),
    path('user/', EmployeeViewSet.as_view({"post": "post"})),
    path('user/', EmployeeViewSet.as_view({"get": "get"})),
    path('company/<int:id>/', CompanyViewSet.as_view({"get": "show"})),
    path('user/<str:username>/', EmployeeViewSet.as_view({"get": "show", "delete": "delete"})),
]
