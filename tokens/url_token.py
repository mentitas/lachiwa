from backend.url_creator import create_url

def generate_url(mail, note, name, redirect):

    print()
    print(f"URL token generated: {create_url(mail, note, name, redirect)}")
    print(f"A notification containing '{note}' will arrive to '{mail}' when the URL is opened, and then it will redirect to {redirect}")
    print(f"If {redirect} isn't a valid url, it will redirect to a dummy page")
    print(f"You can change '{name}' to anything and it will still work the same.")
    print()