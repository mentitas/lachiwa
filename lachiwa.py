#!/bin/python3

from backend.colors import blue, cyan, header, yellow
import tokens.pdf_token as pdf_token
import tokens.url_token as url_token
import tokens.exe_token as exe_token
import tokens.qr_token  as qr_token
import tokens.ini_token as ini_token
import argparse
import re

lachiwa_banner = r"""       __            _     _               
      / /  __ _  ___| |__ (_)_      ____ _ 
     / /  / _` |/ __| '_ \| \ \ /\ / / _` |
    / /__| (_| | (__| | | | |\ V  V / (_| |
    \____/\__,_|\___|_| |_|_| \_/\_/ \__,_|
    A tool to create Honey Tokens."""

def main():
    
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=header(lachiwa_banner))
    
    parser.add_argument('format', choices=['pdf', 'url', 'qr', 'exe', 'ini'], help=cyan("Supported token types."))

    # Requerido para todos los tokens
    parser.add_argument('mail', help = cyan("Notification mail."))                                         
    parser.add_argument('note', help = cyan("Notification note."))

    # Opcional para todos los tokens
    parser.add_argument('-name', help=blue("Optional token file name. Default=token."), default="token")

    # Usado únicamente por url token 
    parser.add_argument('-redirect', help=blue("URL to redirect."), default="")  

    args = parser.parse_args()

    # Chequeamos que redirect es un url válido
    # Regex que saqué de internet, quizás convenga buscar otro
    valid_urls = re.compile('(https?|ftp|file)?://[a-z0-9+&@#/%?=~_|!:,.;]+.[a-z+&@#/%=~_|]', re.IGNORECASE)   
    if not valid_urls.match(args.redirect) and args.redirect != "":
        print(f"{yellow('Warning')}: redirect url isn't valid.")
        args.redirect = ""

    if args.format == "pdf":
        pdf_token.generate_pdf(args.mail, args.note, args.name + ".pdf", args.redirect)
    elif args.format == "url":
        url_token.generate_url(args.mail, args.note, args.name, args.redirect)    
    elif args.format == "exe":
        exe_token.generate_exe(args.mail, args.note, args.name, args.redirect)    
    elif args.format == "qr":
        qr_token.generate_qr(args.mail, args.note, args.name, args.redirect)    
    elif args.format == "ini":
        ini_token.generate_ini(args.mail, args.note, args.redirect, args.name)

    ### Printeamos los resultados

    # Cambio los colores
    note  = cyan(args.note)
    mail  = cyan(args.mail)
    name  = blue(args.name)
    
    print(f"A notification containing '{note}' will arrive to '{mail}'", end= ' ')

    if format == "pdf":
        print(f"when the token is opened with Adobe Acrobat,", end= ' ')
    elif format == "url":
        print(f"when the URL is opened,", end= ' ')    
    elif format == "exe":
        print(f"when the token is executed,", end= ' ')    
    elif format == "qr":
        print(f"when the QR is opened,", end= ' ')    
    else:
        print(f"when the folder containing the token is opened,", end= ' ')

    print("and then it will redirect to", end= ' ')

    if args.redirect == "":
        print("a dummy page.")
        print(f"You can specify where to redirect with -r {cyan('<valid url>')}.\n")
    else:
        print(f"{cyan(args.redirect)}.\n")

if __name__ == "__main__":
    main()