import mimetypes
import urllib.parse
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler


BASE_DIR = Path()
# Створення HTTP Server:
class MyFirstFramework(BaseHTTPRequestHandler):

    def do_GET(self):
        route = urllib.parse.urlparse(self.path)           # наш роутер
        match route.path:                                  # маршрут path
            case '/':                                      # наша case структура
                self.send_html('index.html')
            case '/message.html':  # наша case структура
                self.send_html('message.html')
            case _:
                file = BASE_DIR.joinpath(route.path[1:])
                if file.exists():                           # якщо файл існує (метод exists):
                    self.send_static(file)                 # передаємо цей файл
                else:                                      # якщо не існує: передаємо помилку 404
                    self.send_html(filename='error.html', status_code=404)

        print(urllib.parse.urlparse(self.path))            # шлях обробки наших маршрутів(path,params,query,fragment)

    def do_POST(self):
        pass

    # функція для читання всіх наших html файлів (filename-ім'я відповідного файлу)
    def send_html(self, filename, status_code=200):
        self.send_response(status_code)
        self.send_header(keyword='Content-Type', value='text/html')
        self.end_headers()
        with open(filename, 'rb') as file:                   # відправляємо на читання наш файл(filename).html
            self.wfile.write(file.read())                    # за доп. методу read читаємо файл.html


    # функція обробки статичних файлів
    def send_static(self, filename, status_code=200):
        self.send_response(status_code)
        mime_type, *_ = mimetypes.guess_type(filename)
        if mime_type:
            self.send_header('Content-Type', mime_type)
        else:
            self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        with open(filename, 'rb') as file:
            self.wfile.write(file.read())


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











