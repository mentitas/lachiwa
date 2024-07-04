# ini_token_generator.py

import os
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from backend.cryptogra import encrypt

def generate_ini(mail, note, redirect, name):
    # Load public key from file (assuming pub-key.pem is your public key file)
    with open("backend/pub-key.pem", "rb") as key_file:
        public_pem = key_file.read()
        public_key = load_pem_public_key(public_pem)

    # Encrypt data
    encrypted_data = encrypt(f"{mail}@@@{note}@@@{redirect}", public_key)

    # Construct desktop.ini content
    # acà tengo 127.0.0.1 hay que cambiar si quieren utilizar 0.0.0.0
    desktop_ini_content = f"""
    [.ShellClassInfo]
    IconResource=http://127.0.0.1:8080/{encrypted_data},0
    """

    # Directory to save the desktop.ini file
    directory = os.path.join(os.getcwd(), name)

    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Write desktop.ini file
    ini_file_path = os.path.join(directory, "desktop.ini")
    with open(ini_file_path, "w", encoding="utf-16") as ini_file:
        ini_file.write(desktop_ini_content)

    print(f"Desktop.ini file created at {ini_file_path}")

