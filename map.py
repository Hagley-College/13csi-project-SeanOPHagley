import json
import os
from PIL import Image, ImageTk

from vec2d import Vec2d
from player import Player



map_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),"./maps/"))

class Map():
    
    

    def __init__(self,map_name) -> None:
        
        map_path = os.path.normpath(os.path.join(map_folder,os.path.normpath(map_name)))
        print(map_path)
        map_file_path = os.path.join(map_path,"map.json")
        map_file = open(map_file_path,"r")
        self.map_json = json.loads(map_file.read())
        map_file.close()

        self.tile_size = self.map_json["tile_size"]


        map_file_json = self.map_json["map"]
        self.canvas_size = [0,0]

        self.canvas_size[1] = len(map_file_json)
        self.map = []
        
        for row in map_file_json:
            if len(row) > self.canvas_size[0]:
                self.canvas_size[0] = len(row)

        self.map = []
        i = 0
        for row in map_file_json:
            ir = 0
            self.map.append([])
            for objects in row:
                self.map[i].append([])
                for object in objects:
                    self.map[i][ir].append([object["texture"],object["collisions"]])
                ir += 1
            i += 1


        self.player = Player(Vec2d(self.map_json["player"]["x"],self.map_json["player"]["y"]),self.map_json["player"]["texture"])


        self.textures = []
        texture_file_folder = os.path.join(map_path,"assets")
        i = 0
        for texture_path in self.map_json["texture_paths"]:
            self.textures.append(Image.open(os.path.join(texture_file_folder,texture_path)).resize((self.tile_size, self.tile_size)))
            i += 1

    def query_tile_collision(self,pos) -> bool:

        if not isinstance(pos,Vec2d):
            raise TypeError("map.query_tile_collision only accepts vec2d")
        
        tile = self.map[pos.y][pos.x]

        for object in tile:
            if object[1]:
                return True
        return False
    def set_player_pos(self,pos):
        if not isinstance(pos,Vec2d):
            raise TypeError("map.set_player_pos only accepts vec2d")
        self.player.setPos(pos)

    def __repr__(self) -> str:
        s = ""
        for row in self.map:
            for column in row:
                if column[0][1]:
                    s = s + "#"
                else:
                    s = s + "_"
            s = s+"\n"
        return s

if __name__ == "__main__":
    map = Map("default")
    print(map)
    print(map.query_tile_collision(Vec2d(1,0)))