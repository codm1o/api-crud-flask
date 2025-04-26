# API CRUD Simples com Flask

Este é um projeto básico de uma API CRUD usando Flask, mantendo os dados em memória.

## Pré-requisitos

Instale as dependências:

pip install -r requirements.txt

python app.py

## Como rodar o projeto

1. Instale o Flask:

2. Rode o app:

3. A API estará disponível em: `http://127.0.0.1:5000/`

## Endpoints

### Listar usuários
- **GET** `/users`
- Retorna a lista de todos os usuários.

### Criar usuário
- **POST** `/users`
- Envie um JSON no body da requisição:
```json
{
 "name": "Nome do usuário"
}

