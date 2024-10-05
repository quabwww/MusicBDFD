# Usa la imagen oficial de Python como base
FROM python:3.12-slim

# Instala FFmpeg
RUN apt-get update && apt-get install -y ffmpeg && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requirements
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto
COPY . .

# Exponer el puerto que utiliza FastAPI
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
