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
├── Controller/                # Camada de controle: define as rotas e lógica de entrada/saída HTTP
│   ├── __init__.py
│   └── UserController.py      # Endpoints relacionados a usuários
│
├── Models/                   # Define os modelos do banco de dados (SQLAlchemy)
│   ├── __init__.py
│   ├── Base.py               # Classe base para os modelos ORM
│   ├── Claim.py              # Modelo de permissão/claim
│   ├── Role.py               # Modelo de função/cargo de usuário
│   ├── User.py               # Modelo de usuário
│   └── UserClaim.py          # Associação entre usuários e claims
│
├── Repository/               # Acesso ao banco de dados
│   ├── __init__.py
│   └── DatabaseRepository.py # Funções de CRUD e queries

├── Schemas/               # Define os objetos usados para entrada e saída de dados
│   ├── __init__.py
│   └── RequestResponse.py    # Estrutura padrão de resposta da APIpy # Funções de CRUD e queries
│
├── Services/                 # Camada de regras de negócio
│   ├── __init__.py
│   └── UserService.py        # Lógica de negócio para operações de usuário
│
├── Utils/                    # Utilitários auxiliares
│   ├── __init__.py
│   ├── Logger.py             # Configuração de logging da aplicação
│   └── StartDataBase.py      # Inicialização do banco e criação das tabelas
│
├── main.py                   # Arquivo principal para execução da aplicação Flask
├── requirements.txt          # Lista de dependências do projeto
├── .gitignore                # Arquivos/pastas ignoradas pelo Git
├── app.log                   # Arquivo de log gerado pela aplicação
├── .env                      # Variáveis de ambiente (configurações sensíveis)
└── README.md                 # Documentação do projeto
```

---

## ⚙️ Como Rodar o Projeto

### 1. Configurar Banco de Dados PostgreSQL

1. Baixe o PostgreSQL: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads  
2. Siga o instalador padrão e **anote sua senha e porta escolhidas**.
    2.1 Na pagina "Setup - PostgresSQL", clique em "Next"<br>
    2.2 Na pagina "Installation Directory", escolha o que mais te agrade, ou mantenha o padrão, então clique em "Next"<br>
    2.3 Na pagina "Select Components", não mude nada e clique em Next"<br>
    2.4 Na pagina "Data Directory", scolha o que mais te agrade, ou mantenha o padrão, então <br>
    2.5 Na pagina "Password", digite a senha que gostaria para que seu usuario possa acessar o bannco. **IMPORTANTE: Guarde essa senha, pois vamos usalá mais tarde**
    2.6 Na pagina "Port", escolha a porta que gostaria que o Postgres usasse, ou mantenha a padrão (5432), então clique em "Next" **IMPORTANTE: Guarde essa senha, pois vamos usalá mais tarde**<br>
    2.7 Na pagina "Advanced Options" clique em "Next"<br>
    2.8 Na pagina "Pre Installation Summary" clique em ""Next"<br>
    2.9 Na pagina "Ready to Install" clique em "Next"<br>
    2.10 Aguarde a instalação finalizar<br>
    2.11 Na pagina "Completing the PostgresSQL Setup Wizard", pode desmarcar o radio e então clicar em "Finish"<br>
3. Você pode usar o banco `postgres` padrão ou criar um novo.

📺 *Dica*: [Veja esse vídeo passo-a-passo](https://www.youtube.com/watch?v=4qH-7w5LZsA)

### 2. Configurar o Ambiente Python

1. Clone o projeto usando a linha de comando
```bash
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
- Antes de realizar os testes, foi populada a tabela `roles` , ja que a tabela `users` usa uma chave estrangeira da tabela anterior. 
Exemplos:
```SQL
INSERT INTO roles (id, description)
VALUES
  (1, 'Dono'),
  (2, 'Gerente'),
  (3, 'Funcionário');
```
---

## 🧪 Testes

- Para testar, use o **Insomnia**, **Postman** ou qualquer ferramenta de requisições HTTP.

1. Tentando criar usuario sem nome: <br>
Requisição: http://127.0.0.1:5000/user/<br>
Body:
```json
{
	"email" : "testedono@empresa.com",
	"roleId" : "1"
}
```
Resultado:
![Resultado do Teste](testImages/teste1.png)
2. Tentando criar usuario sem nome, email: <br>
Requisição: http://127.0.0.1:5000/user/ <br>
Body:
```json
{
	"roleId" : "1"
}
```
![Resultado do Teste](testImages/teste2.png)
3. Tentando criar usuario sem nome, email,roleId: <br>
Requisição: http://127.0.0.1:5000/user/ <br>
Body:
```json
{
}
```
![Resultado do Teste](testImages/teste3.png)
4. Tentando criar usuario sem email,roleId:<br>
Requisição: http://127.0.0.1:5000/user/ <br>
Body:
```json
{
    "name" : "Teste",
}
```
![Resultado do Teste](testImages/teste4.png)
5. Tentando criar usuario sem email: <br>
Requisição: http://127.0.0.1:5000/user/ <br>
Body:
```json
{
    "name" : "Teste",
    "roleId": 1
}
```
![Resultado do Teste](testImages/teste5.png)
6. Tentando criar usuario sem roleId: <br>
Requisição: http://127.0.0.1:5000/user/ <br>
Body:
```json
{
    "name" : "Teste",
    "email": "testedono@gmail.com"
}
```
![Resultado do Teste](testImages/teste6.png)
7. Tentando criar usuario com nome vazio: <br>
Requisição: http://127.0.0.1:5000/user/ <br>
Body:
```json
{
    "name" : "",
    "email": "testedono@gmail.com",
    "roleId": 1
}
```
![Resultado do Teste](testImages/teste7.png)
8. Tentando criar usuario com email invalido: <br>
Requisição: http://127.0.0.1:5000/user/ <br>
Body:
```json
{
    "name" : "Joao",
    "email": "teste",
    "roleId": 1
}
```
![Resultado do Teste](testImages/teste8.png)
9. Tentando criar usuario com roleId sem ser um numero: <br>
Requisição: http://127.0.0.1:5000/user/ <br>
Body:
```json
{
    "name" : "Joao",
    "email": "testedono@gmail.com",
    "roleId": "a"
}
```
![Resultado do Teste](testImages/teste9.png)
10. Tentando criar usuario com roleId inexistente: <br>
Requisição: http://127.0.0.1:5000/user/ <br>
Body:
```json
{
    "name" : "Joao",
    "email": "testedono@gmail.com",
    "roleId": 10
}
```
![Resultado do Teste](testImages/teste10.png)
11. Criando usuario com sucesso: <br>
Requisição: http://127.0.0.1:5000/user/ <br>
Body:
```json
{
    "name" : "Joao",
    "email": "testedono@gmail.com",
    "roleId": 1
}
```
![Resultado do Teste](testImages/teste11.png)
![Resultado do Teste](testImages/teste11_2.png)
12. Criando usuario com senha com sucesso: <br>
Requisição: http://127.0.0.1:5000/user/ <br>
Body:
```json
{
    "name" : "Joao",
    "email": "testedono@gmail.com",
    "roleId": 1,
    "password" : "teste"
}
```
![Resultado do Teste](testImages/teste12.png)
![Resultado do Teste](testImages/teste12_2.png)

13. Obtendo roles de um usuario existente: <br>
Requisição: http://127.0.0.1:5000/user/1/getRoles <br>
![Resultado do Teste](testImages/teste13.png)

14. Tentando obter roles de um userId invalido:<br>
Requisição: http://127.0.0.1:5000/user/aaaaa/getRoles <br>
![Resultado do Teste](testImages/teste14.png)

15. Tentando obter roles de um userId inexistente: <br>
Requisição: http://127.0.0.1:5000/user/100/getRoles <br>
![Resultado do Teste](testImages/teste15.png)
---
