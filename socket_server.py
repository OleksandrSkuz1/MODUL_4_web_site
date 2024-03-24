import socket
import json
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STORAGE_DIR = os.path.join(BASE_DIR, 'storage')

class SocketServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('localhost', 5000))
        self.running = True

    def run(self):
        while self.running:
            data, _ = self.socket.recvfrom(1024)
            message = json.loads(data.decode('utf-8'))
            self.process_message(message)

    def process_message(self, message):
        message['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        with open(os.path.join(STORAGE_DIR, 'data.json'), 'a') as f:
            json.dump(message, f)
            f.write('\n')

    def stop(self):
        self.running = False
        self.socket.close()
