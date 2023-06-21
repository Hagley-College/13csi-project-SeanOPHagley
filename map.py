import json

from vec2d import Vec2d
from player import Player

map_folder = ".\\maps\\"

class Map():
    
    

    def __init__(self,map_name) -> None:
        map_file = open(map_folder + map_name + "\\map.json","r")
        self.map_json = json.loads(map_file.read())
        map_file.close()

        self.tile_size = self.map_json["tile_size"]
        self.player = Player(Vec2d(self.map_json["player"]["x"],self.map_json["player"]["y"]),self.map_json["player"]["texture"])
        textures = []
        map = [[]]
        print(self.player)

