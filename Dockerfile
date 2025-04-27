# Usar imagem oficial do Python
FROM python:3.10

# Definir a pasta /app dentro do container
WORKDIR /app

# Copiar todos os arquivos do projeto pra dentro do container
COPY . .

# Instalar dependências
RUN pip install -r requirements.txt

# Expor a porta que o Flask usa
EXPOSE 5000

# Comando para rodar o app quando o container iniciar
CMD ["python", "app.py"]
