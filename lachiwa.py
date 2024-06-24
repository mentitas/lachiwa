import tokens.pdf_token as pdf_token
import tokens.excel_token as excel_token
import tokens.url_token as url_token
import argparse

def main():
    parser = argparse.ArgumentParser(description="A tool to generate Honeytokens.")
    
    parser.add_argument('format', choices=['pdf', 'excel', 'url'], help="Supported token types.")
    parser.add_argument('mail',      help="Notification mail.")                                          # Requerido para todos los tokens
    parser.add_argument('note',      help="Notification note.")                                          # Requerido para todos los tokens
    parser.add_argument('-name',     help="Optional token file name. Default=token.", default="token")   # Opcional para todos los tokens
    parser.add_argument('-redirect', help="URL to redirect. Only applies to url tokens.", default="https://google.com")  # Requerido únicamente para url token

    args = parser.parse_args()
    
    match args.format:
        case "pdf":
            pdf_token.generate_pdf(args.mail, args.note, args.name + ".pdf")
        case "excel":
            excel_token.generate_excel(args.mail, args.note, args.name + ".xls")
        case "url":
            url_token.generate_url(args.mail, args.note, args.name, args.redirect)


if __name__ == "__main__":
    main()