from backend.url_creator import create_url
from backend.colors import blue
import qrcode

def generate_qr(mail, note, name, redirect):

    # Llama a create_url y guarda el url resultante en un QR
    img = qrcode.make(create_url(mail, note, name, redirect))
    img.save(f"{name}.png")

    name     = blue(name + ".png")

    print(f"\nQR token generated: {name}\n")