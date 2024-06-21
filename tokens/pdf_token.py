from fpdf import FPDF

def generate_pdf(mail, note, name):
    #cosas con backend
    
    
    #generar pdf
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Comic Sans", size=30)
    pdf.cell(200, 10, txt="Has sido hackeado por chusma", ln=True, align='C')
    pdf.set_text_color(0, 0, 255)
    pdf.output(name)
    print(f"PDF token generado: {name}")