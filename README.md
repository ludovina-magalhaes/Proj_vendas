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

```mermaid
graph TD;
    A[Arquivo Excel (.xls)] --> B[Extração];
    B --> C[Transformação];
    C --> D[Carga no PostgreSQL];
    D --> E[DBeaver para gerenciamento];
    E --> F[Análise e Visualização (VSCode / Jupyter)];
    G[Pipeline automatizado] --> H[Render - Deploy e Execução];
Extração: Leitura dos dados diretamente do arquivo Excel.

Transformação: Limpeza e preparação dos dados em Python.

Carga: Dados inseridos em tabelas no banco PostgreSQL.

Gerenciamento: DBeaver utilizado para consultas e manutenção do banco.

Análise: Desenvolvida em VSCode com Jupyter notebooks.

Deploy: Pipeline executado e agendado via Render, utilizando variáveis do arquivo .env.

Tecnologias Utilizadas
Python (pandas, sqlalchemy, psycopg2)

PostgreSQL (banco de dados relacional)

DBeaver (ferramenta GUI para PostgreSQL)

VSCode (IDE para desenvolvimento)

Render (plataforma de deploy e execução automatizada)

Arquivo .env para configuração segura de variáveis de ambiente

Configuração do Ambiente
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/ludovina-magalhaes/Proj_vendas.git
Configure o arquivo .env com as variáveis necessárias para conexão ao banco e outras credenciais, exemplo:

ini
Copiar
Editar
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nome_do_banco
DB_USER=usuario
DB_PASSWORD=senha
Crie o ambiente virtual e instale as dependências:

bash
Copiar
Editar
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows
pip install -r requirements.txt
Execute os scripts/notebooks na ordem:

Extração do arquivo Excel

Transformação dos dados

Carga no PostgreSQL

Análise exploratória e visualização

Estrutura do Repositório
bash
Copiar
Editar
Proj_vendas/
│
├── data/                 # Arquivos Excel e dados processados
├── notebooks/            # Notebooks Jupyter para análise
├── scripts/              # Scripts Python para pipeline ETL
├── .env                  # Variáveis de ambiente (não versionar)
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação
Deploy e Automação
O pipeline está configurado para ser executado automaticamente na plataforma Render.

Variáveis de ambiente sensíveis são gerenciadas via .env.

O banco de dados PostgreSQL pode ser acessado e gerenciado via DBeaver para consultas, validação e manutenção.

Referências
pandas documentation

SQLAlchemy documentation

psycopg2 documentation

PostgreSQL documentation

DBeaver website

Render documentation

Autor
Ludovina Magalhães
GitHub
Portfolio
