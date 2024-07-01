import re
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from backend.cryptogra import encrypt

# Cargamos la pem pública de un archivo
key_file = open("backend/pub-key.pem", "r")
public_pem = key_file.read()
public_pem = bytes(public_pem, "utf-8")

# Obtenemos la clave pública
public_key = load_pem_public_key(public_pem)

def create_url(mail, note, name="", redirect=""):

    # Regex que saqué de internet, quizás convenga buscar otro
    valid_urls = re.compile('(https?|ftp|file)?://[a-z0-9+&@#/%?=~_|!:,.;]+.[a-z+&@#/%=~_|]', re.IGNORECASE)   
    if not valid_urls.match(redirect):
        redirect = ""

    message  = str(mail + "@@@" + note + "@@@" + redirect)
    enc_data = encrypt(message, public_key)

    # Si le agregás cosas en el medio, las ignora!
    # http://0.0.0.0:8080/enc_data es equivalente a http://0.0.0.0:8080/basura/enc_data

    if name == "":
        return "http://0.0.0.0:8080/" + enc_data              # TODO: Cambiar la IP por la IP pública
    else:
        return "http://0.0.0.0:8080/" + name + "/" + enc_data # TODO: Cambiar la IP por la IP pública