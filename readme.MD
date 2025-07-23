# Backend Challenge Shipay

## Feito Por:
Artur Valladares Hernandez Giacummo

## Visão Geral

Esse projeto visa estruturar uma API Rest usando Python para resolver os exercicios 3,4 e 5 propostos no desafio.

## Endpoints Disponiveis
/User : Metodo POST --> Fornecer no body da requisição um JSON com a seguinte estrutura:
{
    "name": str
    "email": str
    "roleId: int
    "password": str?
}
Caso não forneça uma senha, ela será gerada automaticamente -> Cria um novo usuario

/User/{userId}/Roles : Metodo GET -> fornecer o id do usuario no link -> Retorna o Role_Id do usuario em questão

## Estrutura do Projeto

Nessa seção será explicada a estrutura dos arquivos do projeto e o papel de cada um.

```
Desafio-Backend-Shipay/
│
├── Controller/
|    ├── __init__.py
|    ├── UserController.py
├── Models/
|   ├── __init__.py
|   ├── Base.py
|   ├── Claim.py
|   ├── RequestResponse.py
|   ├── Role.py
|   ├── User.py
|   ├── UserClaim.py
├── Repository/
|   ├── __init__.py
|   ├── DatabaseRepository.py
├── Services/
|   ├── __init__.py
|   ├── UserService.py
├── Utils/
|   ├── __init__.py
|   ├── StartDataBase.py
├── main.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

## Como Rodar o Projeto
### Configuração Banco SQL (Sugestão PostgresSQL)
1. Faça download do PostgresSQL no link abaixo:
https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

2. Ao terminar o download, execute o instalador
3. Na pagina "Setup - PostgresSQL", clique em "Next"
4. Na pagina "Installation Directory", escolha o que mais te agrade, ou mantenha o padrão, então clique em "Next"
5. Na pagina "Select Components", não mude nada e clique em Next"
6. Na pagina "Data Directory", scolha o que mais te agrade, ou mantenha o padrão, então 
7. Na pagina "Password", digite a senha que gostaria para que seu usuario possa acessar o bannco. **IMPORTANTE: Guarde essa senha, pois vamos usalá mais tarde**
8. Na pagina "Port", escolha a porta que gostaria que o Postgres usasse, ou mantenha a padrão (5432), então clique em "Next" **IMPORTANTE: Guarde essa senha, pois vamos usalá mais tarde**
9. Na pagina "Advanced Options" clique em "Next"
10. Na pagina "Pre Installation Summary" clique em ""Next"
11. Na pagina "Ready to Install" clique em "Next"
12. Aguarde a instalação finalizar
13. Na pagina "Completing the PostgresSQL Setup Wizard", pode desmarcar o radio e então clicar em "Finish"

**OBS: Caso tenha ficado com alguma duvida, siga o passo a passo do video abaixo:**
https://www.youtube.com/watch?v=4qH-7w5LZsA

### Configuração Python
1. Crie um arquivo .env e adicione o valor: 
**Exemplo para PostgresSQL**
```
DATABASE_URL: "postgresql://{usuario}:{senha}@{ip}:{port}/{db}" 
Onde:
usuario = usuario que pode acessar o banco (apos a instalação, existe um usuario padrão chamado postgres, mas , se quiser, fique a vontade para criar outro)
senha = senha do usuario que pode acessar o banco (configurado na instalação)
ip = IP em que o Postgres esta hospedado (se estiver rodando local, pode colocar o valor localhost)
port = Porta em que o Postgres esta rodando (configurado na instalação)
db = Nome do Banco de Dados (apos concluir a instalação, existe um banco padrão de nome postgres, mas se quiser fique a vontade para criar outro)
```
2. Execute o seguinte comando:
```
pip install -r requirements.txt
```

3. Com isso, tudo deve estar preparado para rodar o projeto. Então, basta executar o comando

```
python main.py
```
## Testes e Resultados
Para realizar os testes, usarei o Insonia para simular as chamadas HTTP para a API.