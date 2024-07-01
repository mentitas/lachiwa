from http.server import BaseHTTPRequestHandler, HTTPServer
from cryptography.fernet import Fernet
from mail_sender import send_email
import time
import os

# Obtengo la ruta del archivo key.txt relativa a la ubicacion de server.py
# Esto es mas que nada para hacer que corra el docker
base_dir = os.path.dirname(os.path.abspath(__file__))
key_file_path = os.path.join(base_dir, 'key.txt')
with open(key_file_path, "r") as key_file:
    key = key_file.read().strip()
    key = bytes(key, "utf-8")

t = Fernet(key)

hostName   = "0.0.0.0"
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

        enc_request = bytes(enc_request, "utf-8")

        try:
            # La desencripto y la formateo adecuadamente
            dec_request = str(t.decrypt(enc_request)) # Esto puede generar una excepción, porque la request puede ser inválida
            dec_request = str(dec_request)[2:-1]

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