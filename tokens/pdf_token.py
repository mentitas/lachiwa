from fpdf import FPDF
#from PyPDF2 import PdfReader, PdfWriter # Para cielo
from pypdf import PdfReader, PdfWriter # Para rosu
from backend.url_creator import create_url
from backend.colors import cyan, blue

def generate_pdf(mail, note, name, redirect):
    # Crear el PDF con FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=30)
    pdf.cell(200, 10, txt="Has sido lachiweado por chusma", ln=True, align='C')
    pdf.set_text_color(21, 60, 200)
    pdf.output(name)

    # Leer el PDF generado y añadir JavaScript
    reader = PdfReader(name)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    # This url looks kind of like Adobe Support and it redirects you to the actual Adobe Support.
    evil_url = create_url(mail, note, "helpx.adobe/support/", "https://helpx.adobe.com/support/acrobat.html")
    
    url = create_url(mail, note, redirect)
    writer.add_js(f"app.launchURL('{url}', true);")

    with open(name, "wb") as f:
        writer.write(f)

    note     = cyan(note)
    mail     = cyan(mail)
    redirect = cyan(redirect)
    name     = blue(name)
    
    print(f"\nPDF token generated: {name}\n")