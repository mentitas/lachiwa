from openpyxl import load_workbook

def generate_excel(mail, note, name):
    f_name = {name},'.xlsx'
    workbook = load_workbook(filename= f_name, keep_vba=True) 
    sheet = workbook.active
    sheet['A1'] = 'Has sido hackeado por chusma'