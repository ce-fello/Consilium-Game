import socket
from source.server.Player import Player
from source.server.Economics import Economics


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))
client.send('I`m client\n'.encode())
from_server = client.recv(4096).decode()
player = Player(int(from_server), 'Alexey',
                Economics([10, 10, 10, 10, 10, 10], [2, 2, 2, 2, 2, 2],
                          [0.9, 0.9, 0.9, 0.9, 0.9, 0.9]))

client.close()
