from rest_framework.test import APITestCase
from rest_framework import status


class CompanyTestCase(APITestCase):

    def no_cnpj_test(self):
        data = {
            "company_name": "los hermanos",
            "trading_name": "los hermanos",
            "employees": [1]
        }

        response = self.client.post('/company/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def no_company_name(self):
        data = {
            "cnpj": "1234848775",
            "trading_name": "los hermanos",
            "employees": [1]
        }

        response = self.client.post('/company/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

