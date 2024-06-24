from cryptography.fernet import Fernet

key_file = open("backend/key.txt", "r")
key = key_file.read()
key = bytes(key, "utf-8")

t = Fernet(key)

def create_url(mail, note, name="", redirect=""):

    enc_data = t.encrypt(bytes(mail + "/" + note + "/" + redirect, "utf-8"))    
    enc_data = str(enc_data)[2:-1]

    # Si le agregás cosas en el medio, las ignora!
    # http://0.0.0.0:8080/basura/enc_data es equivalente a http://0.0.0.0:8080/enc_data

    if name == "":
        return "http://0.0.0.0:8080/" + enc_data              # TODO: Cambiar la IP por la IP pública
    else:
        return "http://0.0.0.0:8080/" + name + "/" + enc_data # TODO: Cambiar la IP por la IP pública

import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Generar honeytokens en diferentes formatos.")
    parser.add_argument('mail',      help="Mail de notificación")
    parser.add_argument('note',      help="Mensaje para la notificación")
    parser.add_argument('-name',     help="Nombre opcional para el url", default="") 
    parser.add_argument('-redirect', help="A que url redireccionar",     default="") 

    args = parser.parse_args()

    print("\nThe following url will send an email to " + str(args.mail) + " with the note '" + str(args.note) + "'\n")
    
    url = create_url(args.mail, args.note, args.name, args.redirect)
    print(url)

if __name__ == "__main__":
    main()