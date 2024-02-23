# Sistema de estoque :computer:
Projeto de TCC com o objetivo de criar um sistema de estoque para diversas empresas com um administrador geral

## Tecnologias :toolbox:
Tecnologias utilizadas no projeto:
* [Python 3.12+](https://www.python.org/downloads/)
* [Docker](https://www.docker.com/)
* [FastAPI](https://fastapi.tiangolo.com/pt/)
* [SQL Serve](https://www.microsoft.com/pt-br/sql-server/sql-server-downloads)
* [Vue.js](https://vuejs.org/)
* [Devexpress](https://js.devexpress.com/Vue/)

## Instalação :hammer_and_wrench:
### Com Docker :whale2:
Clone o repositorio do projeto
```bash
  git clone https://github.com/leo-jansen/estoque_tcc.git
  cd estoque_tcc
```
Coloque as variaveis de ambiente no arquivo `/api/.env`, existe o arquivo `/api/.env-sample` com um exemplo das variaveis necessárias

Suba os containers usando o docker-compose
```bash
  docker-compose up --build -d
```
Abra o navegador e digite `http://localhost/login` e use um do usuarios no arquivo `/config/script_eqtl.sql` a senha irá ser `Teste@123`
