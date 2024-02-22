import socket

class udp_server:
    def __init__(self, port):
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.bind(('localhost', self.port))
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            data, addr = self.server.recvfrom(1024)
            data = data.decode('utf-8')
            print(f"Получил: {data} от {addr}")
            self.server.sendto("ок", addr)

    def stop(self):
        self.running = False
