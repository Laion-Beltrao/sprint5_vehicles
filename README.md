# sprint5_vehicles
O foco desse projeto é que você tenha mais prática com tarefas comuns de engenharia de software. Isso vai aprimorar e complementar suas habilidades de dados

## Criar um repositório no GitHub.
- .gitignore - python
- arquivo README.md


## Clonar o repositório do GitHub.
- git clone URL_do_repositório_do_github


## Criar um ambiente virtual na pasta de  origem do projeto.
- conda create --name vehicles_env # Criar ambiente virtual
- conda activate vehicles_env # Ativar o ambient virtual
- conda deactivate # Desativar o ambiente virtual
- conda env list # Visualisar todos os ambientes virtuais
- conda install PACOTE # Instalar pacotes

- python3 --version # Verificar se o python está instalado
- python3 -m venv nome_do_ambiente # Criar o ambiente virtual
- source nome_do_ambiente/bin/activate # Ativar o ambiente virtual
- pip install pandas # Instalar pacotes
- deactivate # Desativar ambiente virtual


## Instalar pacotes através do arquivo requirements.txt
- touch requirements.txt # Criar arquivo requirements.txt
- Adicionar todos os pacotes necessário no projeto nesse arquivo
    - pandas
    - streamlit
    - plotly-express
- pip install -r requirements.txt # Instalar os pacotes


## Subir projeto para o GitHub
- git init . # Inicializa um repositório Git no diretório atual.
- git status # Mostra o estado atual do seu repositório Git
- git add . # Adiciona TODOS os arquivos do diretório atual para a área de preparação
- git commit -m "commit inicial" # Adiciona uma mensagem