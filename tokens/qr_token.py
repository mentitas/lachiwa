from backend.url_creator import create_url
from backend.colors import cyan, blue
import qrcode

def generate_qr(mail, note, name, redirect):

    # Llama a create_url y guarda el url resultante en un QR
    img = qrcode.make(create_url(mail, note, name, redirect))
    img.save(f"{name}.png")

    note     = cyan(note)
    mail     = cyan(mail)
    redirect = cyan(redirect)
    name     = blue(name + ".png")

    print()
    print(f"QR token generated: {name}")
    print(f"A notification containing '{note}' will arrive to '{mail}' when the QR is opened, and then it will redirect to {redirect}")
    print(f"If {redirect} isn't a valid url, it will redirect to a dummy page")
    print()