from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

### Este archivo inicializa la clave pública y privada del servidor

# Esto es lo que tiene el servidor
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Esto es lo que tienen las lachiwas
public_key = private_key.public_key()

priv_pem = private_key.private_bytes(
	encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

pub_pem = public_key.public_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Ojo: no entiende que \n = enter.
key_file = open("priv-key.pem", "w")
key_file.write(str(priv_pem).replace("\\n", "\n")[2:-1])

key_file = open("pub-key.pem", "w")
key_file.write(str(pub_pem).replace("\\n", "\n")[2:-1])