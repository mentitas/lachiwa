from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter

def generate_pdf(mail, note, name):
    # Crear el PDF con FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=30)
    pdf.cell(200, 10, txt="Has sido hackeado por chusma", ln=True, align='C')
    pdf.set_text_color(21, 60, 200)
    pdf.output(name)

    # Leer el PDF generado y añadir JavaScript
    reader = PdfReader(name)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    # JavaScript para enviar un correo 
    # cambiar para que se envie a un servidor propio
    js = f"""
    app.launchURL('www.google.com', true);
    """

    writer.add_js(js)

    with open(name, "wb") as f:
        writer.write(f)

    print(f"PDF token generado: {name}")

