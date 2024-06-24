from backend.url_creator import create_url
import qrcode

def generate_qr(mail, note, name, redirect):

    # Llama a create_url y guarda el url resultante en un QR

    img = qrcode.make(create_url(mail, note, name, redirect))
    img.save(f"{name}.png")

    print()
    print(f"QR token generated: {name}.png")
    print(f"A notification containing '{note}' will arrive to '{mail}' when the QR is opened, and then it will redirect to {redirect}")
    print()