from backend.url_creator import create_url

def generate_url(mail, note, name, redirect):

    # Chequea que redirect es un url válido y luego llama a create_url

    # TODO:
    # redirect debe empezar con "http://" o "https://"
    # y debe terminar con ".com" o similar

    print()
    print(f"URL token generated: {create_url(mail, note, name, redirect)}")
    print(f"A notification containing '{note}' will arrive to '{mail}' when the URL is opened, and then it will redirect to {redirect}")
    print(f"You can change '{name}' to anything and it will still work the same.")
    print()