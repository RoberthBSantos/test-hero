from rest_framework import serializers
from company.models import Company
from user.serializers import EmployeeSerializer

from user.models import Employee


class CompanySerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = (
            'company_name',
            'cnpj',
            'trading_name',
            'employees'
        )

    # def get_employees(self,obj):
    #     return obj.user_django.username


class CompanyCreateSerializer(serializers.ModelSerializer):
    employees = serializers.ListField(write_only=True)

    def validate(self, data):
        if Company.objects.filter(cnpj=data.get("cnpj")).exists():
            raise serializers.ValidationError({"cnpj": "Já existe um cadastro para este cnpj"})
        if Company.objects.filter(company_name=data.get("company_name")).exists():
            raise serializers.ValidationError({"company_name": "Já existe uma cadastro para esta razão social."})
        if Company.objects.filter(trading_name=data.get("trading_name")).exists():
            raise serializers.ValidationError({"trading_name": "Já existe um cadastro para este nome fantasia."})

        if data.get("employees"):
            for employee in data.get("employees"):
                try:
                    Employee.objects.get(id=employee)

                except:
                    raise serializers.ValidationError(
                        {"employees": "Algum dado de funcionário está errado."})
        return data

    class Meta:
        model = Company
        fields = (
            'id',
            'company_name',
            'trading_name',
            'cnpj',
            'employees'
        )

    def create(self, validated_data):
        print(validated_data)
        company = Company(
            company_name=validated_data["company_name"],
            trading_name=validated_data["trading_name"],
            cnpj=validated_data["cnpj"]
        )
        company.save()
        if validated_data["employees"]:
            for employee in validated_data["employees"]:
                company.employees.add(employee)
        company.save()
        return company


class EmployeesListSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            'id',
            'username',
            'cpf'
        )

    def get_username(self, obj):
        return obj.user_danjo_id.username
