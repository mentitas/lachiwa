import sys
from cryptography.fernet import Fernet
import argparse

key_file = open("key.txt", "r")
key = key_file.read()
key = bytes(key, "utf-8")

t = Fernet(key)

def main():
    parser = argparse.ArgumentParser(description="Generar honeytokens en diferentes formatos.")
    parser.add_argument('mail', help="Mail de notificación")
    parser.add_argument('note', help="Mensaje para la notificación")

    args = parser.parse_args()

    test_enc_request = t.encrypt(bytes(args.mail + "/" + args.note, "utf-8"))
    print("\nThe following url will send an email to " + str(args.mail) + " with the note '" + str(args.note) + "'\n")
    print("http://0.0.0.0:8080/" + str(test_enc_request)[2:-1] + "\n")

if __name__ == "__main__":
    main()