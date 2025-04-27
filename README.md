# API CRUD Simples com Flask

## 1. Pré-requisitos

- Python 3.8 ou superior
- Git (opcional, para versionamento)


## 2. Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/codm1o/api-crud-flask.git
   cd api-crud-flask
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```


## 3. Como rodar

1. Inicie o servidor:
   ```bash
   python app.py
   ```
2. Abra no navegador ou cliente REST:
   ```
   http://127.0.0.1:5000/
   ```


## 4. Endpoints

### 4.1 Listar usuários

- **GET** `/users`
- Retorna a lista de todos os usuários cadastrados.

#### Exemplo de resposta
```json
[]
```


### 4.2 Criar usuário

- **POST** `/users`
- Body (JSON):
  ```json
  {
    "name": "Nome do usuário"
  }
  ```
- Retorna o novo usuário com `id` gerado.

#### Exemplo de resposta
```json
{
  "id": 1,
  "name": "Nome do usuário"
}
```


### 4.3 Deletar usuário

- **DELETE** `/users/{id}`
- Remove o usuário com o `id` especificado.

#### Exemplo de resposta
```json
{
  "message": "Usuário deletado com sucesso"
}
```

*Desenvolvido por [codm1o](https://github.com/codm1o) — 2025*

