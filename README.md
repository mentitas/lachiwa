# lachiwa

Para levantar el docker de lachiwa, se debe ejecutar el siguiente comando:
```bash
docker build -t lachiwa . 
docker run -p 8000:80 -d lachiwa
docker exec -it <id-contenedor> python backend/server.py
```