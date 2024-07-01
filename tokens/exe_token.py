import PyInstaller.__main__
import os
import shutil
import subprocess
from backend.url_creator import create_url

def generate_exe(mail, note, name):
    
    url = create_url(mail,note)
    
    os.makedirs("./temp_folder")
    os.chdir("./temp_folder")

#     
#     script = f"""
# import webbrowser
# webbrowser.open('{url}')
#     """
    
    script = f"""print("hola")"""
    nombre_archivo = name + ".py"

    # Abrir el archivo en modo escritura y guardar el contenido
    with open(nombre_archivo, "w") as archivo:
        archivo.write(script)

    # subprocess.run(["pyinstaller", nombre_archivo, "--onefile", "--windowed", "--distpath", "dist", "--workpath", "build", "--specpath", "build"], capture_output=False)  
    PyInstaller.__main__.run([
        nombre_archivo,
        '--onefile',
        '--windowed',
        '--distpath', 'dist', 
        '--workpath', 'build',
        '--specpath', 'build'
    ])

    os.chdir("..")
    os.rename(f"temp_folder/dist/{name}", f"{name}")
    shutil.rmtree("./temp_folder")

    # Agarramos el ejecutable de la carpeta "dist" y lo movemos fuera de la carpeta actual
