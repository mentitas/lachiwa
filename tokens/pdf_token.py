from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter

def generate_pdf(mail, note, name):
    # Crear el PDF con FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Comic Sans", size=30)
    pdf.cell(200, 10, txt="Has sido hackeado por chusma", ln=True, align='C')
    pdf.set_text_color(21, 60, 200)
    pdf.output(name)

    # Leer el PDF generado y añadir JavaScript
    reader = PdfReader(name)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    # JavaScript para enviar un correo 
    #cambiar para que se envie a un servidor propio
    js = f"""
    var mail = "{mail}";
    var note = "{note}";
    var subj = "PDF Abierto";
    var body = "El PDF ha sido abierto.";
    this.submitForm({{
        cURL: "mailto:" + mail + "?subject=" + subj + "&body=" + body,
        cSubmitAs: "PDF",
        cCharSet: "utf-8"
    }});
    """

    writer.add_js(js)

    with open(name, "wb") as f:
        writer.write(f)

    print(f"PDF token generado: {name}")

