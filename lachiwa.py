import tokens.pdf_token as pdf_token
import tokens.excel_token as excel_token
import argparse

def main():
    parser = argparse.ArgumentParser(description="Generar honeytokens en diferentes formatos.")
    parser.add_argument('format', choices=['pdf', 'excel'], help="Formato del token a generar")
    parser.add_argument('mail', help="Mail de notificación")
    parser.add_argument('name', help="Nombre de archivo a generar")
    parser.add_argument('note', help="Mensaje para la notificación")

    args = parser.parse_args()
    
    if args.format == "pdf":
        pdf_token.generate_pdf(args.mail, args.note, args.name)
    elif args.format == "excel":
        excel_token.generate_excel(args.mail, args.note, args.name)

if __name__ == "__main__":
    main()