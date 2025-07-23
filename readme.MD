# Backend Challenge Shipay

## Feito Por:
**Artur Valladares Hernandez Giacummo**

## Visão Geral

Este projeto tem como objetivo estruturar uma API REST em Python para resolver os exercícios 3, 4 e 5 propostos no desafio da Shipay.

## 🧩 Endpoints Disponíveis

### Criar Usuário
**POST** `/user`  
Body (JSON):
```json
{
  "name": "string",
  "email": "string",
  "roleId": int,
  "password": "string (opcional)"
}
```
- Se a senha não for fornecida, será gerada automaticamente.
- Retorna se conseguiu cirar o usuario ou não

### Obter Role de um Usuário
**GET** `/user/{userId}/roles`  
- Forneça o ID do usuário na URL.
- Retorna todos os `role_id` do usuário correspondente.

---

## 🗂️ Estrutura do Projeto

```
Desafio-Backend-Shipay/
│
├── Controller/
│   ├── __init__.py
│   └── UserController.py
│
├── Models/
│   ├── __init__.py
│   ├── Base.py
│   ├── Claim.py
│   ├── RequestResponse.py
│   ├── Role.py
│   ├── User.py
│   └── UserClaim.py
│
├── Repository/
│   ├── __init__.py
│   └── DatabaseRepository.py
│
├── Services/
│   ├── __init__.py
│   └── UserService.py
│
├── Utils/
│   ├── __init__.py
│   ├── Logger.py
│   └── StartDataBase.py
│
├── main.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

---

## ⚙️ Como Rodar o Projeto

### 1. Configurar Banco de Dados PostgreSQL

1. Baixe o PostgreSQL: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads  
2. Siga o instalador padrão e **anote sua senha e porta escolhidas**.
2.1 Na pagina "Setup - PostgresSQL", clique em "Next"
2.2 Na pagina "Installation Directory", escolha o que mais te agrade, ou mantenha o padrão, então clique em "Next"
2.3 Na pagina "Select Components", não mude nada e clique em Next"
2.5 Na pagina "Data Directory", scolha o que mais te agrade, ou mantenha o padrão, então 
2.5 Na pagina "Password", digite a senha que gostaria para que seu usuario possa acessar o bannco. **IMPORTANTE: Guarde essa senha, pois vamos usalá mais tarde**
2.6 Na pagina "Port", escolha a porta que gostaria que o Postgres usasse, ou mantenha a padrão (5432), então clique em "Next" **IMPORTANTE: Guarde essa senha, pois vamos usalá mais tarde**
2.7 Na pagina "Advanced Options" clique em "Next"
2.8 Na pagina "Pre Installation Summary" clique em ""Next"
2.9 Na pagina "Ready to Install" clique em "Next"
2.10 Aguarde a instalação finalizar
2.11 Na pagina "Completing the PostgresSQL Setup Wizard", pode desmarcar o radio e então clicar em "Finish"
3. Você pode usar o banco `postgres` padrão ou criar um novo.

📺 *Dica*: [Veja esse vídeo passo-a-passo](https://www.youtube.com/watch?v=4qH-7w5LZsA)

### 2. Configurar o Ambiente Python

1. Clone o projeto usando a linha de comando
```
git clone https://github.com/arturstaation/Desafio-Backend-Shipay.git
```

2. Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
DATABASE_URL=postgresql://<usuario>:<senha>@<host>:<porta>/<database>
```

3. Substitua os campos conforme abaixo:

| Campo        | Descrição                                                                 |
|--------------|---------------------------------------------------------------------------|
| `<usuario>`  | Nome de usuário do seu banco de dados PostgreSQL.                         |
| `<senha>`    | Senha do usuário do banco.                                                |
| `<host>`     | Endereço do servidor (por exemplo: `localhost` ou um IP como `127.0.0.1`).|
| `<porta>`    | Porta do PostgreSQL (geralmente `5432`).                           |
| `<database>` | Nome do banco de dados que você criou (ex: `Teste`).                      |

Exemplo real:
```env
DATABASE_URL=postgresql://postgres:123@localhost:5432/Teste
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Execute a aplicação:
```bash
python main.py
```

---

## 📌 Observações

- As tabelas são criadas automaticamente com base nos modelos definidos em `Models/`.
- Antes de realizar os testes, foi populada a tabela `roles` , ja que a tabela `users` usa uma chave estrangeira da tabela anterior. Exemplos:
---

## 🧪 Testes

- Para testar, use o **Insomnia**, **Postman** ou qualquer ferramenta de requisições HTTP.

---
