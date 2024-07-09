# Usa una imagen base de Python
FROM python:3.10.0

WORKDIR /lachiwa

# Copia todo el código fuente del proyecto al contenedor
COPY server.py        ./
COPY lachiwa.py       ./
COPY requirements.txt ./
COPY ./backend ./backend
COPY ./tokens  ./tokens

RUN pip install --no-cache-dir -r /lachiwa/requirements.txt

# Expone el puerto en el que el servidor funciona
EXPOSE 3000

# Cambio esta variable para tener logs
ENV PYTHONUNBUFFERED=1

# Comando para ejecutar el servidor por defecto
CMD ["python3", "server.py"]