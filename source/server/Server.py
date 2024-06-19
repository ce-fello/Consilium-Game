import socket
from source.server.Game import Game
from source.server.Player import Player
from source.server.Map_parser import *


# alexey_player = Player(1, 'Alexey')
# sergey_player = Player(2, 'Sergey')
# players = [alexey_player, sergey_player]
# game = Game(players, create_map('../resources/map.txt'))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8080))
server.listen(5)
names_for_players = ['Alexey', 'Sergey', 'Ivan', 'Anton']
id_max = 1
connected_ids = []
while True:
    connection, address = server.accept()
    from_client = ''
    while True:
        data = connection.recv(4096)
        if not data:
            break
        from_client += data.decode('utf8')
        print(f'From client: {from_client}')
        connection.send(f'{id_max};'.encode())
        connected_ids.append(id_max)
        id_max += 1
    connection.close()
    print('client disconnected and shutdown')
