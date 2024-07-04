from http.server import BaseHTTPRequestHandler, HTTPServer
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend
from cryptogra import decrypt

from mail_sender import send_email
import time
import os

with open("priv-key.pem", 'rb') as pem_in:
    pemlines = pem_in.read()
    private_key = load_pem_private_key(pemlines, None, default_backend())

hostName   = "0.0.0.0"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    
    def do_GET(self):    
        
        # Recibo la request encriptada y la separo según "/"
        path = self.path.split("/")

        enc_request = path[-1] if path[-1] else path[-2]
        try:
            # La desencripto y la formateo adecuadamente
            dec_request = decrypt(enc_request, private_key)
            mail, note, redirect = dec_request.split("@@@")
            ip = self.client_address[0]

            print(f"\nYou are connecting from {ip}")
            print(f"We'll send a mail to {mail}")
            print(f"saying {note}\n")

            if redirect == "":
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(f"<p>You are connecting from {ip}</p>", "utf-8"))
                self.wfile.write(bytes(f"<p>We'll send a mail to {mail}</p>", "utf-8"))
                self.wfile.write(bytes(f"<p>saying '{note}'</p>", "utf-8"))

            else:
                self.send_response(302)
                self.send_header('Location', redirect)
                self.end_headers()

            # Descomentar la siguiente linea para que se mande un mail cuando se accede a la url
            send_email("mail-server@lachiwa.com", mail, "Han accedido tu honey token desde la IP " + ip, note)

        except:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<p>Error, wrong token provided</p>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")