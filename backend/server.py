from http.server import BaseHTTPRequestHandler, HTTPServer
from cryptography.fernet import Fernet
from mail_server import send_email
import time

# Consigo la clave de encriptación
key_file = open("key.txt", "r")
key = key_file.read()
key = bytes(key, "utf-8")

t = Fernet(key)

hostName   = "0.0.0.0"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    
    def do_GET(self):    

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Recibo la request encriptada
        enc_request = bytes(self.path[1:], "utf-8")

        try:
            # La desencripto y la formateo adecuadamente
            dec_request = str(t.decrypt(enc_request)) # Esto puede generar una excepción, porque la request puede ser inválida
            dec_request = str(dec_request)[2:-1]

            # Transformo la request en un array
            mail, note = dec_request.split("/")
            ip = self.client_address[0]

            self.wfile.write(bytes("<p> You are connecting from %s </p>" % ip, "utf-8"))
            self.wfile.write(bytes("<p>We'll send a mail to %s" % mail, "utf-8"))
            self.wfile.write(bytes("<p>saying '%s'"             % note, "utf-8"))

            # Descomentar la siguiente linea para que se mande un mail cuando se accede a la url
            # send_email("mail-server@lachiwa.com", mail, "Han accedido tu honey token desde la IP " + ip, note)


        except:
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
