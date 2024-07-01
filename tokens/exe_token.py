import PyInstaller.__main__
import os
import shutil
import subprocess
from backend.url_creator import create_url

def generate_exe(mail, note, name, redirect):
    
    url = create_url(mail,note,redirect)
    
    current_dir = os.getcwd()
    os.makedirs("/tmp/lachiwa")
    os.chdir("/tmp/lachiwa")

    script = f"""
import webbrowser
webbrowser.open('{url}')
"""
    
    # Abrir el archivo en modo escritura y guardar el contenido
    with open("file.py", "w") as archivo:
        archivo.write(script)
    
    DEVNULL = subprocess.DEVNULL
    output=subprocess.check_output(f"pyinstaller --onefile file.py",shell=True, stderr = DEVNULL , stdin = DEVNULL )

    shutil.move("/tmp/lachiwa/dist/file", f"{current_dir}/{name}")
    shutil.rmtree("/tmp/lachiwa")

    print()
    print(f"EXE token generated: {name}")
    print(f"A notification containing '{note}' will arrive to '{mail}' when the token is executed.")
    print()
