# Usa una imagen base de Python
FROM python:3.10.0

WORKDIR /lachiwa

COPY requirements.txt /lachiwa/requirements.txt
RUN pip install --no-cache-dir -r /lachiwa/requirements.txt

# Copia todo el código fuente del proyecto al contenedor
COPY . /TP

# Expone el puerto en el que el servidor funciona
EXPOSE 8000

# Comando para ejecutar el servidor por defecto
CMD ["python3", "./backend/server.py"]