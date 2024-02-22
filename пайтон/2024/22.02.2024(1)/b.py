import socket

class udp_client:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, message):
        self.client.sendto(message.encode('utf-8'), (self.server_address, self.server_port))

    def receive(self):
        data = self.client.recvfrom(1024)
        data = data.decode('utf-8')
        return data
