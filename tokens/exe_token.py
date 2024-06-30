import PyInstaller.__main__

from url_creator_sin_cripto import create_url

def generate_exe(mail, note, name):
    
    url = create_url(mail,note)
    
    script = f"""
import webbrowser
webbrowser.open('{url}')
"""
    
    nombre_archivo = name + ".py"

    # Abrir el archivo en modo escritura y guardar el contenido
    with open(nombre_archivo, "w") as archivo:
        archivo.write(script)
    
    PyInstaller.__main__.run([
        nombre_archivo,
        '--onefile',
        '--windowed'
    ])
