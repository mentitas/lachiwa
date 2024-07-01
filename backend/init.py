from cryptography.fernet import Fernet

key = Fernet.generate_key()

key_file = open("key.txt", "w")
key_file.write(str(key)[2:-1]) 

# TODO: Cambiar para que todos los lachiwas tengan la clave pública del server. Luego, el server desencripta con su clave privada.