import mimetypes
import urllib.parse
import socket
import json
import threading
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
from socket_server import SocketServer
from client_server import main as run_client

BASE_DIR = Path()

# Створення HTTP Server:
class MyFirstFramework(BaseHTTPRequestHandler):

    def do_GET(self):
        route = urllib.parse.urlparse(self.path)           # наш роутер
        match route.path:                                  # маршрут path
            case '/':                                      # наша case структура
                self.send_html('index.html')
            case '/message.html':
                self.send_html('message.html')
            case _:
                file = BASE_DIR.joinpath(route.path[1:])
                if file.exists():                          # якщо файл існує (метод exists):
                    self.send_static(file)                 # передаємо цей файл
                else:                                      # якщо не існує: передаємо помилку 404
                    self.send_html(filename='error.html', status_code=404)

        print(urllib.parse.urlparse(self.path))            # шлях обробки наших маршрутів(path,params,query,fragment)


# Функція обробки POST-запитів та відправки даних на сокет сервер:
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_data_dict = urllib.parse.parse_qs(post_data.decode('utf-8'))  # Парсимо POST-дані у словник

        # Відправляємо дані на сокет сервер
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.sendto(json.dumps(post_data_dict).encode('utf-8'), ('localhost', 5000))


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

# Функція для запуску серверу
def run_server():
    address = ('localhost', 8080)
    http_server = HTTPServer(address, MyFirstFramework)

    # Запускаємо сокет сервер у окремому потоці
    socket_server = SocketServer()
    socket_server.start()

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
        socket_server.stop()


if __name__ == '__main__':
    # запуск клієнтського сервера у окремому потоці
    client_thread = threading.Thread(target=run_client)
    client_thread.start()

    # запуск основного HTTP і сокет серверів
    run_server()













