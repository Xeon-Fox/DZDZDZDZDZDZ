from a import udp_server
from b import udp_client

server = udp_server(12345)
server.start()

client = udp_client('localhost', 12345)
client.send("салам")
print(client.receive()) 

server.stop()