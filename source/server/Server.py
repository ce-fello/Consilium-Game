import socket
from source.server.Game import Game
from source.server.Player import Player
from source.server.Map_parser import *
import threading
import pickle
from source.server.Packet import ClientPacket, ServerPacket


host = '26.92.111.70'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()


clients = []
nicknames = []


# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)


# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(ClientPacket('{} left!'.format(nickname)))
            nicknames.remove(nickname)
            break


# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send(pickle.dumps(ServerPacket('NICK')))
        client_packet = pickle.loads(client.recv(4096))
        nicknames.append(client_packet.name)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(client_packet.name))
        client.send(pickle.dumps(ClientPacket('Connected to server!')))
        broadcast(pickle.dumps(ClientPacket("{} joined!".format(client_packet.name))))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
