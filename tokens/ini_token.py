import os
from backend.url_creator import create_url
from backend.colors import blue

def generate_ini(mail, note, redirect, name):

    url = create_url(mail, note, redirect)

    desktop_ini_content = f"""
    [.ShellClassInfo]
    IconResource=http://{url},0
    """

    # Directory to save the desktop.ini file
    directory = os.path.join(os.getcwd(), name)

    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Write desktop.ini file
    ini_file_path = os.path.join(directory, "desktop.ini")
    with open(ini_file_path, "w", encoding="utf-16") as ini_file:
        ini_file.write(desktop_ini_content)

    print(f"\nINI token generated: {blue(ini_file_path)}\n")