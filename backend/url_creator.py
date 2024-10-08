from cryptography.hazmat.primitives.serialization import load_pem_public_key
from backend.cryptogra import encrypt

### Este archivo define la función create_url

# Cargamos la pem pública de un archivo
key_file = open("backend/pub-key.pem", "r")
public_pem = key_file.read()
public_pem = bytes(public_pem, "utf-8")

# Obtenemos la clave pública
public_key = load_pem_public_key(public_pem)

def create_url(mail, note, name="", redirect=""):

    message  = str(mail + "@@@" + note + "@@@" + redirect)
    enc_data = encrypt(message, public_key)

    # Si le agregás cosas en el medio, las ignora!
    # http://0.0.0.0:8080/enc_data es equivalente a http://0.0.0.0:8080/basura/enc_data

    if name == "":
        return "http://0.0.0.0:8080/" + enc_data
    else:
        return "http://0.0.0.0:8080/" + name + "/" + enc_data