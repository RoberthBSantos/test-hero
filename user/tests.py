from rest_framework.test import APITestCase
from rest_framework import status


class FuncionarioTestCase(APITestCase):

    def no_cpf(self):
        data = {
            "username": "xlanne",
            "password": "senhasecreta"
        }

        response = self.client.post('/user/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def no_username(self):
        data = {
            "cpf": "92874206347",
            "password": "senhasecreta"
        }

        response = self.client.post('/user/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cadastro_sem_password(self):
        data = {
            "nome_completo": "Eren Jaeger",
            "username": "tatakae",
        }

        response = self.client.post('/user/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_successful(self):
        data = {
            "cpf": "92874206347",
            "username": "xlanne",
            "password": "senhasecreta"
        }

        response = self.client.post('/user/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_employees(self):
        response = self.client.get('/user/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

