import keyword
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler


# Створення HTTP Server:
class MyFirstFramework(BaseHTTPRequestHandler):

    def do_GET(self):
        route = urllib.parse.urlparse(self.path)         # наш роутер
        match route.path:                                # маршрут path
            case '/':                                    # наша case структура


        print(urllib.parse.urlparse(self.path))          # шлях обробки наших маршрутів(path,params,query,fragment)

    def do_POST(self):
        pass

    # функція для читання всіх наших html файлів (filename-ім'я відповідного файлу)
    def sent_html(self, filename, status_code=200):
        self.send_response(status_code)
        self.send_header(keyword: '')
        self.end_headers()
        with open(filename, 'rb') as file:               # відправляємо на читання наш файл(filename).html
            self.wfile.write(file.read())                # за доп. методу read читаємо файл.html


# функція для запуску серверу
def run_server():
    address = ('localhost', 8080)
    http_server = HTTPServer(address, MyFirstFramework)
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server.close()



if __name__ == '__main__':
    run_server()











