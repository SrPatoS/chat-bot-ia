# Usar uma imagem oficial do Python
FROM python:3.10

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos do projeto para dentro do container
COPY . /app

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando para rodar a aplicação
CMD ["python", "src/start.py"]
