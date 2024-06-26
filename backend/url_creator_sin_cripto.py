import re

def create_url(mail, note, name="", redirect=""):

    # Regex que saqué de internet, quizás convenga buscar otro
    valid_urls = re.compile('(https?|ftp|file)?://[a-z0-9+&@#/%?=~_|!:,.;]+.[a-z+&@#/%=~_|]', re.IGNORECASE)   
    if not valid_urls.match(redirect):
        redirect = ""

    data = str(mail + "%" + note + "%" + redirect)

    if name == "":
        return "http://0.0.0.0:8080/" + data              # TODO: Cambiar la IP por la IP pública
    else:
        return "http://0.0.0.0:8080/" + name + "/" + data # TODO: Cambiar la IP por la IP pública