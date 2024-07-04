from backend.url_creator import create_url
from backend.colors import colors

def generate_url(mail, note, name, redirect):

    url = colors.OKBLUE + create_url(mail, note, name, redirect) + colors.ENDC

    print()
    print(f"URL token generated: {url}")
    print()

    note     = colors.OKCYAN + note     + colors.ENDC
    mail     = colors.OKCYAN + mail     + colors.ENDC
    redirect = colors.OKCYAN + redirect + colors.ENDC
    name     = colors.OKCYAN + name     + colors.ENDC
    
    print(f"A notification containing '{note}' will arrive to '{mail}' when the URL is opened, and then it will redirect to {redirect}")
    print(f"If {redirect} isn't a valid url, it will redirect to a dummy page")
    print(f"You can change '{name}' to anything and it will still work the same.")
    print()