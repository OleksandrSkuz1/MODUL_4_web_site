import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class MyFirstFramework(BaseHTTPRequestHandler):

    # GET POST PUT PATCH DELETE
    def do_GET(self):
        route = urllib.parse.urlparse(self.path)
        match route.path:
            case '/':


        self.send_response(200)
        self.end_headers()
        with open('index.html', 'rb') as file:
            self.wfile.write(file.read())

    def do_POST(self):
        pass

def run_server():
    address = ('localhost', 5000)
    http_server = HTTPServer(address, MyFirstFramework)
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()


if __name__ == '__main__':
    run_server()











