from cryptography.fernet import Fernet

key_file = open("backend/key.txt", "r")
key = key_file.read()
key = bytes(key, "utf-8")

t = Fernet(key)

def create_url(mail, note, name="", redirect=""):

    # TODO: Chequear que redirect es un url válido
    # redirect debe empezar con "http://" o "https://"
    # y debe terminar con ".com" o similar
    
    enc_data = t.encrypt(bytes(mail + "#" + note + "#" + redirect, "utf-8"))    
    enc_data = str(enc_data)[2:-1]

    # Si le agregás cosas en el medio, las ignora!
    # http://0.0.0.0:8080/enc_data es equivalente a http://0.0.0.0:8080/basura/enc_data

    if name == "":
        return "http://0.0.0.0:8080/" + enc_data              # TODO: Cambiar la IP por la IP pública
    else:
        return "http://0.0.0.0:8080/" + name + "/" + enc_data # TODO: Cambiar la IP por la IP pública