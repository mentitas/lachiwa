from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend
from cryptogra import decrypt

from http.server import BaseHTTPRequestHandler, HTTPServer
from mail_sender import send_email
import time
import os

with open("priv-key.pem", 'rb') as pem_in:
    pemlines = pem_in.read()
    private_key = load_pem_private_key(pemlines, None, default_backend())

hostName   = "0.0.0.0" # TODO: Pasar la dirección como parámetro
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    
    def do_GET(self):    
        
        # Recibo la request encriptada y la separo según "/"
        path = self.path.split("/")

        enc_request = ""
        # La request encriptada es el último dato no nulo del path
        for p in path:
            if p != "":
                enc_request = p
        
        try:
            # La desencripto y la formateo adecuadamente
            dec_request = decrypt(enc_request, private_key)
            
            mail, note, redirect = dec_request.split("@@@")
            ip = self.client_address[0]

            print("")
            print("You are connecting from " + ip)
            print("We'll send a mail to "    + mail)
            print("saying "                  + note)
            print("")

            if redirect == "":
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                self.wfile.write(bytes("<p> You are connecting from %s </p>" % ip, "utf-8"))
                self.wfile.write(bytes("<p>We'll send a mail to %s" % mail, "utf-8"))
                self.wfile.write(bytes("<p>saying '%s'"             % note, "utf-8"))

            else:
                
                self.send_response(302)
                self.send_header('Location', redirect)
                self.end_headers()

            # Descomentar la siguiente linea para que se mande un mail cuando se accede a la url
            # send_email("mail-server@lachiwa.com", mail, "Han accedido tu honey token desde la IP " + ip, note)

        except:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<p>Error, wrong token provided</p>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")