from backend.url_creator import create_url
from backend.colors import cyan, blue

def generate_url(mail, note, name, redirect):

    url = blue(create_url(mail, note, name, redirect))

    print(f"\nURL token generated: {url}\n")