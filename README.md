# Projeto de Análise de Vendas

Repositório do projeto de análise de vendas online de artigos artesanais, com pipeline completo ETL, análise exploratória e visualização, utilizando integração com banco de dados PostgreSQL e deploy na plataforma Render.

---

## Conteúdo

- **Extração:** Dados extraídos de arquivos Excel (.xls).
- **Transformação:** Tratamento, limpeza e preparação dos dados.
- **Carga:** Inserção dos dados tratados no banco de dados PostgreSQL.
- **Análise:** Visualizações e estatísticas para insights de vendas.
- **Deploy:** Pipeline automatizado hospedado na plataforma Render.
- **Ambiente:** Configuração via arquivo `.env` para credenciais e conexões.

---

## Arquitetura ETL

   A --> [Arquivo Excel (.xls)]
   B --> [Extração];
   C --> [Carga no PostgreSQL];
   D --> [DBeaver para gerenciamento];
   E --> [Análise e Visualização (VSCode / Jupyter)];
   F --> [Pipeline automatizado] 
   H --> [Render - Deploy e Execução];


Extração: Leitura dos dados diretamente do arquivo Excel.

Transformação: Limpeza, normalização e preparação dos dados usando Python.

Carga: Inserção dos dados transformados em tabelas do banco PostgreSQL.

Gerenciamento: Acesso e manutenção do banco via DBeaver.

Análise: Desenvolvimento das análises em VSCode com Jupyter notebooks.

Deploy: Pipeline automatizado na Render, utilizando variáveis definidas no .env.

Tecnologias Utilizadas:
- Python (pandas, SQLAlchemy, psycopg2)
- PostgreSQL (banco de dados relacional)
- DBeaver (ferramenta GUI para PostgreSQL)
- VSCode (IDE para desenvolvimento)
- Render (plataforma de deploy e execução automatizada)

git clone https://github.com/ludovina-magalhaes/Proj_vendas.git
Configure o arquivo .env com as variáveis necessárias para conexão ao banco e outras credenciais, exemplo:

![image](https://github.com/user-attachments/assets/9e7c8ee4-dc47-4063-91fc-493bd084215a)


Crie o ambiente virtual e instale as dependências:
python -m venv env
pip install -r requirements.txt
Execute os scripts/notebooks na ordem:

Extração do arquivo Excel

Transformação dos dados

Carga no PostgreSQL

Análise exploratória e visualização

Estrutura do Repositório

![image](https://github.com/user-attachments/assets/414f7991-6d02-4638-8b2f-7ca31f5e0fd9)

Deploy e Automação
O pipeline está configurado para ser executado automaticamente na plataforma Render.

Variáveis de ambiente sensíveis são gerenciadas via .env.

O banco de dados PostgreSQL pode ser acessado e gerenciado via DBeaver para consultas, validação e manutenção.

## Referências

- [pandas documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [SQLAlchemy documentation](https://docs.sqlalchemy.org/)
- [psycopg2 documentation](https://www.psycopg.org/docs/)
- [PostgreSQL documentation](https://www.postgresql.org/docs/)
- [DBeaver website](https://dbeaver.io/)
- [Render documentation](https://render.com/docs)


Autor
Ludovina Magalhães

