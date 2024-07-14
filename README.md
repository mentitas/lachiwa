# Lachiwa

Para levantar el docker de lachiwa, se debe ejecutar el siguiente comando:
```bash
docker build -t lachiwa .
docker run -p 8080:8080 lachiwa:latest
```

Luego, desde otra terminal, se puede testear la aplicación asi:
```bash
python lachiwa.py [-h] [-name NAME] [-redirect REDIRECT] {pdf,url,qr,exe,ini} mail note

```