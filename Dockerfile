# Usamos Python 3.11 liviano como base
FROM python:3.11-slim

# Definimos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos primero el archivo de dependencias
COPY requirements.txt .

# Instalamos las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código al contenedor
COPY . .

# Variable de entorno para la API key (se pasa al correr el contenedor)
ENV BALLDONTLIE_API_KEY=""

# Comando que se ejecuta al iniciar el contenedor
CMD ["python", "main.py"]
