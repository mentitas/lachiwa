from backend.url_creator import create_url
from backend.colors import colors
import qrcode

def generate_qr(mail, note, name, redirect):

    # Llama a create_url y guarda el url resultante en un QR
    img = qrcode.make(create_url(mail, note, name, redirect))
    img.save(f"{name}.png")

    note     = colors.OKCYAN + note          + colors.ENDC
    mail     = colors.OKCYAN + mail          + colors.ENDC
    redirect = colors.OKCYAN + redirect      + colors.ENDC
    name     = colors.OKBLUE + name + ".png" + colors.ENDC

    print()
    print(f"QR token generated: {name}")
    print(f"A notification containing '{note}' will arrive to '{mail}' when the QR is opened, and then it will redirect to {redirect}")
    print(f"If {redirect} isn't a valid url, it will redirect to a dummy page")
    print()