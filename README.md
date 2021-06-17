# Teste-Api Company Hero
Repositório destinado para teste da Company Hero

## Detalhes do projeto

* Projeto em Django ultilizando a ferramenta Django- Rest Framework para criar APIs para gerenciamento de cadastro de funcionarios e empresas.

## Endpoints

### Para usar endpoints basta usar os links abaixos seguindo os exemplos:

* POST and GET Empresa: https://company-hero-teste.herokuapp.com/company/

* Exemplo de data para o POST: {
    "company_name": "los hermanos",
    "cnpj": "1234848775",
    "trading_name":"los hermanos",
    "employees":[1]
}  
* Exemplo de url para pegar um indice específico de empresa pelo id: https://company-hero-teste.herokuapp.com/company/1

* POST and GET Funcioario: https://company-hero-teste.herokuapp.com/user/

* Exemplo de data para o POST: { 
    "cpf": "928.742.063-47",
    "username": "xlanner",
    "password": "senha"
    }
* Exemplo de url para pegar um indice específico de funcionário pelo username: https://company-hero-teste.herokuapp.com/user/xlanner Pode-se usar este mesmo endpoint com o metodo DELETE.

## Testes unitários:

* Usados para testar os endpoints

* Clone o projeto para seu ambiente local, instale os requeriments com o comando "pip install -r requeriments.txt"

* para rodar os testes ultilizar o comando python manage.py test

