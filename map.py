import json
import os

from vec2d import Vec2d
from player import Player

map_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),"./maps/"))

class Map():
    
    

    def __init__(self,map_name) -> None:
        
        map_path = os.path.normpath(os.path.join(map_folder,os.path.normpath(map_name)))
        print(map_path)
        map_file_path = os.path.join(map_path,"map.json") # os.path.normpath(os.path.join(map_folder,os.path.normpath(map_name+ "/map.json")))
        map_file = open(map_file_path,"r")
        self.map_json = json.loads(map_file.read())
        map_file.close()

        self.tile_size = self.map_json["tile_size"]
        self.player = Player(Vec2d(self.map_json["player"]["x"],self.map_json["player"]["y"]),self.map_json["player"]["texture"])


        self.textures = []
        texture_file_folder = os.path.join(map_path,"textures")
        for texture_path in self.map_json["texture_paths"]:
            texture_path
        map = [[]]
        print(self.textures)

if __name__ == "__main__":
    map = Map("default")