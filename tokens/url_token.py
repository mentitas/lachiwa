from backend.url_creator import create_url
from backend.colors import cyan, blue

def generate_url(mail, note, name, redirect):

    url = blue(create_url(mail, note, name, redirect))

    print()
    print(f"URL token generated: {url}")
    print()

    note     = cyan(note)
    mail     = cyan(mail)
    redirect = cyan(redirect)
    name     = cyan(name)
    
    print(f"A notification containing '{note}' will arrive to '{mail}' when the URL is opened, and then it will redirect to {redirect}")
    print(f"If {redirect} isn't a valid url, it will redirect to a dummy page")
    print(f"You can change '{name}' to anything and it will still work the same.")
    print()