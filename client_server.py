import socket
import json
import os

def main():
    host = 'localhost'  # Ім'я хоста для підключення до сервера
    port = 5000         # Порт сервера

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Створюємо сокет
    message = input('>>> ')

    while message.lower().strip() != 'quit':
        data = {'message': message}                     # Підготовка даних у форматі JSON
        json_data = json.dumps(data).encode('utf-8')    # Кодуємо дані у формат JSON та перетворюємо у байти
        client_socket.sendto(json_data, (host, port))   # Відправляємо дані на сервер
        message = input('>>> ')

    client_socket.close()

if __name__ == '__main__':
    main()
