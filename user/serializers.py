from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import Employee
from company.models import Company


class CompanysListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'company_name',
            'cnpj',
            'trading_name',

        )


class EmployeeSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    companys = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            'id',
            'username',
            'cpf',
            'companys'
        )

    def get_username(self, obj):

        return obj.user_django.username

    def get_companys(self, obj):
        companys_all = Company.objects.all()
        companys = []
        for company in companys_all:
            for employee in company.employees.all():
                if employee.id == obj.id:
                    companys.append(company)

        return CompanysListSerializer(companys, many=True).data


class EmployeeCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        if User.objects.filter(username=data.get("username")).exists():
            raise serializers.ValidationError({"username": "Nome de usuário já cadastrado."})
        if Employee.objects.filter(cpf=data.get("cpf")).exists():
            raise serializers.ValidationError({"cpf": "Já possui um cadastro para este cpf"})
        return data

    class Meta:
        model = Employee
        fields = (
            'id',
            'username',
            'password',
            'cpf'
        )

    def create(self, validated_data):
        user = User(
            username=validated_data['username'].lower()
        )
        user.set_password(validated_data['password'])
        user.save()
        print(user.id)

        empoloyee = Employee(

            cpf=validated_data['cpf'],
            user_django_id=user.id
        )
        empoloyee.save()
        return empoloyee


class EmployeeUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        if User.objects.filter(username=data.get("username")).exists():
            raise serializers.ValidationError({"username": "Nome de usuário já cadastrado."})

        return data

    class Meta:
        model = Employee
        fields = (
            'id',
            'username',
            'password',
            'cpf'
        )

    def update(self, instance, validated_data):
        instance.user_django_id
