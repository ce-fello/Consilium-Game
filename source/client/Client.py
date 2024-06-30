import socket
from source.server.Player import Player
from source.server.Economics import Economics
import threading
import pickle
from source.server.Packet import ClientPacket, ServerPacket


nickname = input('Введите имя: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('26.92.111.70', 55555))


def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            server_packet = pickle.loads(client.recv(4019))
            if server_packet.name == 'NICK':
                client_packet = pickle.dumps(ClientPacket(nickname))
                client.send(client_packet)
            else:
                print(server_packet.name)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break


# Sending Messages To Server
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))


# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

