from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode

def encrypt(message, public_key):
    enc_data = public_key.encrypt(
        message.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # Encode encrypted data in base64 for safe transport/storage
    return urlsafe_b64encode(enc_data).decode('utf-8')


def decrypt(ciphertext, private_key):
    ciphertext_bytes = urlsafe_b64decode(ciphertext.encode('utf-8'))
    plaintext = private_key.decrypt(
        ciphertext_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # Decode decrypted plaintext from bytes to string
    return plaintext.decode('utf-8')