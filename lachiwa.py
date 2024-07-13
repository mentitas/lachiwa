#!/bin/python3

from backend.colors import blue, cyan, header, yellow
import tokens.pdf_token as pdf_token
import tokens.url_token as url_token
import tokens.exe_token as exe_token
import tokens.qr_token  as qr_token
import tokens.ini_token as ini_token
import argparse
import re
import bleach

lachiwa_banner = r"""       __            _     _               
      / /  __ _  ___| |__ (_)_      ____ _ 
     / /  / _` |/ __| '_ \| \ \ /\ / / _` |
    / /__| (_| | (__| | | | |\ V  V / (_| |
    \____/\__,_|\___|_| |_|_| \_/\_/ \__,_|
    A tool to create Honey Tokens."""

def valid_input(text):
    if "@@@" in text:
        raise argparse.ArgumentTypeError(yellow("Input can't contain '@@@'"))
    # Uso un regex para quitar código html del tipo "<script> ... </script>"
    sanitized_text = re.sub(r'<script\b[^>]*>(.*?)</script>', '', text, flags=re.IGNORECASE)
    # Uso bleach para reemplazar los caracteres especiales por otros
    sanitized_text = bleach.clean(sanitized_text)
    return sanitized_text
    
def valid_url(url):
    # Chequeamos que redirect es un url válido
    valid_urls = re.compile('(https?|ftp|file)?://[a-z0-9+&@#/%?=~_|!:,.;]+.[a-z+&@#/%=~_|]', re.IGNORECASE)   
    if not valid_urls.match(url) and url != "":
        raise argparse.ArgumentTypeError(yellow(f"'{url}' isn't a valid url"))
    return url

def main():
    
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=header(lachiwa_banner))
    
    parser.add_argument('format', choices=['pdf', 'url', 'qr', 'exe', 'ini'], help=cyan("Specify the type of honey token to generate. Choices: 'pdf', 'url', 'qr', 'exe', 'ini'."))

    # Requerido para todos los tokens
    parser.add_argument('mail', type=valid_input, help = cyan("The email address where the notification will be sent when the token is accessed."))                                         
    parser.add_argument('note', type=valid_input, help = cyan("A note to include in the notification email, i.e. a description of the type of token triggered"))

    # Opcional para todos los tokens
    parser.add_argument('-name',                     help=blue("Optional: specify the file name for the token. Default is 'token'."), default="token")
    parser.add_argument('-redirect', type=valid_url, help=blue("Optional: specify a URL to redirect to when the token is accessed. Default is an empty string, which redirects to a dummy page."), default="")  

    args = parser.parse_args()
    
    format = args.format # save the "format" argument to use in following 

    if format == "pdf":
        pdf_token.generate_pdf(args.mail, args.note, args.name + ".pdf", args.redirect)
    elif format == "url":
        url_token.generate_url(args.mail, args.note, args.name, args.redirect)    
    elif format == "exe":
        exe_token.generate_exe(args.mail, args.note, args.name, args.redirect)    
    elif format == "qr":
        qr_token.generate_qr(args.mail, args.note, args.name, args.redirect)    
    elif format == "ini":
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
    elif format == "ini":
        print(f"when the folder containing the token is opened,", end= ' ')

    print("and then it will redirect to", end= ' ')

    if args.redirect == "":
        print("a dummy page.")
        print(f"You can specify where to redirect with -r {cyan('<valid url>')}.\n")
    else:
        print(f"{cyan(args.redirect)}.\n")

if __name__ == "__main__":
    main()