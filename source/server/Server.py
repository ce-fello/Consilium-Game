from source.server.Game import Game
from source.server.Player import Player
from source.server.Map_parser import *


alexey_player = Player(1, 'Alexey')
sergey_player = Player(2, 'Sergey')
players = [alexey_player, sergey_player]
game = Game(players, create_map('../resources/map.txt'))
