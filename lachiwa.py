#!/bin/python3

from backend.colors import blue, cyan, header
import tokens.pdf_token as pdf_token
import tokens.url_token as url_token
import tokens.exe_token as exe_token
import tokens.qr_token  as qr_token
import tokens.ini_token as ini_token
import argparse

lachiwa = r"""     __      __    ___  _   _  ____  _    _    __   
    (  )    /__\  / __)( )_( )(_  _)( \/\/ )  /__\  
     )(__  /(__)\( (__  ) _ (  _)(_  )    (  /(__)\ 
    (____)(__)(__)\___)(_) (_)(____)(__/\__)(__)(__)
    A tool to create Honey Tokens."""

dancinglachiwa = r"""
   _          _         ____    _   _                                  _      
  |"|     U  /"\  u  U /"___|  |'| |'|      ___      __        __  U  /"\  u  
U | | u    \/ _ \/   \| | u   /| |_| |\    |_"_|     \"\      /"/   \/ _ \/   
 \| |/__   / ___ \    | |/__  U|  _  |u     | |      /\ \ /\ / /\   / ___ \   
  |_____| /_/   \_\    \____|  |_| |_|    U/| |\u   U  \ V  V /  U /_/   \_\  
  //  \\   \\    >>   _// \\   //   \\. -,_|___|_,- .-,_\ /\ /_,-.  \\    >>  
 (_")("_) (__)  (__) (__)(__) (_") ("_) \_)-' '-(_/  \_)-'  '-(_/  (__)  (__) 
"""

elegantlachiwa = r"""       __            _     _               
      / /  __ _  ___| |__ (_)_      ____ _ 
     / /  / _` |/ __| '_ \| \ \ /\ / / _` |
    / /__| (_| | (__| | | | |\ V  V / (_| |
    \____/\__,_|\___|_| |_|_| \_/\_/ \__,_|
    A tool to create Honey Tokens."""


epiclachiwa = r""" __        ______    ______    __  __    __    __     __    ______   
/\ \      /\  __ \  /\  ___\  /\ \_\ \  /\ \  /\ \  _ \ \  /\  __ \  
\ \ \____ \ \  __ \ \ \ \____ \ \  __ \ \ \ \ \ \ \/ ".\ \ \ \  __ \ 
 \ \_____\ \ \_\ \_\ \ \_____\ \ \_\ \_\ \ \_\ \ \__/".~\_\ \ \_\ \_\
  \/_____/  \/_/\/_/  \/_____/  \/_/\/_/  \/_/  \/_/   \/_/  \/_/\/_/"""

lachiwa3d = r"""
 __                       __                                  
/\ \                     /\ \      __                         
\ \ \         __      ___\ \ \___ /\_\  __  __  __     __     
 \ \ \  __  /'__`\   /'___\ \  _ `\/\ \/\ \/\ \/\ \  /'__`\   
  \ \ \L\ \/\ \L\.\_/\ \__/\ \ \ \ \ \ \ \ \_/ \_/ \/\ \L\.\_ 
   \ \____/\ \__/.\_\ \____\\ \_\ \_\ \_\ \___x___/'\ \__/.\_\
    \/___/  \/__/\/_/\/____/ \/_/\/_/\/_/\/__//__/   \/__/\/_/
"""

def main():
    
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=header(elegantlachiwa))
    
    parser.add_argument('format', choices=['pdf', 'url', 'qr', 'exe', 'ini'], help="Supported token types.")

    # Requerido para todos los tokens
    parser.add_argument('mail', help = cyan("Notification mail."))                                         
    parser.add_argument('note', help = cyan("Notification note."))

    # Opcional para todos los tokens
    parser.add_argument('-name', help=blue("Optional token file name. Default=token."), default="token")

    # Usado únicamente por url token 
    parser.add_argument('-redirect', help=blue("URL to redirect."), default="https://google.com")  

    args = parser.parse_args()
    
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


if __name__ == "__main__":
    main()