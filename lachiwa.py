import tokens.pdf_token as pdf_token
import tokens.url_token as url_token
import tokens.qr_token as qr_token
import tokens.exe_token as exe_token
# import tokens.excel_token as excel_token
import argparse

def main():
    parser = argparse.ArgumentParser(description="A tool to generate Honeytokens.")
    
    parser.add_argument('format', choices=['pdf', 'excel', 'url', 'qr', 'exe'], help="Supported token types.")

    # Requerido para todos los tokens
    parser.add_argument('mail', help="Notification mail.")                                         
    parser.add_argument('note', help="Notification note.")

    # Opcional para todos los tokens
    parser.add_argument('-name',     help="Optional token file name. Default=token.", default="token")

    # Usado únicamente por url token 
    parser.add_argument('-redirect', help="URL to redirect. Only applies to URL and QR tokens.", default="https://google.com")  

    args = parser.parse_args()
    
    # Todo: cambiar a ifs
    match args.format:
        case "pdf":
            pdf_token.generate_pdf(args.mail, args.note, args.name + ".pdf")
        case "excel":
            print("not supported")
            #excel_token.generate_excel(args.mail, args.note, args.name + ".xls")
        case "url":
            url_token.generate_url(args.mail, args.note, args.name, args.redirect)
        case "qr":
            qr_token.generate_qr(args.mail, args.note, args.name, args.redirect)
        case "exe":
            #print("not supported")
            exe_token.generate_exe(args.mail, args.note, args.name)

if __name__ == "__main__":
    main()