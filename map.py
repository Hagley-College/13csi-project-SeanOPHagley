import json
import os
from PIL import Image, ImageTk

from vec2d import Vec2d
from player import Player



map_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),"./maps/"))

class Map():
    
    

    def __init__(self,map_name) -> None:
        print("before: "+map_name)
        if map_name == "":
            map_name = "default"
        print("after: " + map_name)

        map_path = os.path.normpath(os.path.join(map_folder,os.path.normpath(map_name)))
        #print(map_path)
        map_file_path = os.path.join(map_path,"map.json")
        map_file = open(map_file_path,"r")
        self.map_json = json.loads(map_file.read())
        map_file.close()

        self.tile_size = self.map_json["tile_size"]
        self.goal = Vec2d(self.map_json["goal"]["x"],self.map_json["goal"]["y"])

        map_json = self.map_json["map"]
        self.canvas_size = [0,0]

        self.canvas_size[1] = len(map_json)*self.tile_size
        self.map = []
        
        for row in map_json:
            if len(row) > self.canvas_size[0]:
                self.canvas_size[0] = len(row)*self.tile_size

        self.len = Vec2d(0, len(self.map))

        self.map = []
        i = 0
        for row in map_json:
            ir = 0
            self.map.append([])
            for objects in row:
                self.map[i].append([])
                for object in objects:
                    self.map[i][ir].append([object["texture"],object["collisions"]])
                ir += 1

                if len(row) > self.len.x:
                    self.len.x = len(row)
            i += 1


        self.player = Player(Vec2d(self.map_json["player"]["x"],self.map_json["player"]["y"]),self.map_json["player"]["texture"])


        self.textures = []
        texture_file_folder = os.path.join(map_path,"assets")
        i = 0
        for texture_path in self.map_json["texture_paths"]:
           # print(os.path.normpath(os.path.join(texture_file_folder,texture_path)))
            self.textures.append(Image.open(os.path.normpath(os.path.join(texture_file_folder,texture_path))).resize([self.tile_size,self.tile_size],Image.NEAREST))
            i += 1

        self.texture_paths = []
        i = 0
        for texture_path in self.map_json["texture_paths"]:
            self.texture_paths.append(os.path.normpath(os.path.join(texture_file_folder,texture_path)))
            i += 1

    def query_tile(self,pos):
        if not isinstance(pos,Vec2d):
            raise TypeError("map.query_tile only accepts vec2d")
        
        try:
            tile = self.map[pos.y][pos.x]
        except:
            return None

        return tile

    def query_tile_collision(self,pos) -> bool:

        if not isinstance(pos,Vec2d):
            raise TypeError("map.query_tile_collision only accepts vec2d")

        if pos.x < 0 or pos.y < 0 or pos.y >= len(self.map) or pos.x >= len(self.map[0]):
            return True
        tile = self.map[pos.y][pos.x]


        for object in tile:
            if object[1]:
                return True
        return False

    def query_tile_textures(self,pos):

        if not isinstance(pos,Vec2d):
            raise TypeError("map.query_tile_textures only accepts vec2d")
            re
        
        tile = self.map[pos.y][pos.x]
        textures = []
        for thing in tile:
            textures.append(self.textures[thing[0]])

        return textures

    def move_player(self,direction):
        if not isinstance(direction,Vec2d):
            raise TypeError("map.move_player only accepts vec2d")
        targetlocation = Vec2d(self.player.position.x + direction.x,self.player.position.y + direction.y)
        if not self.query_tile_collision(targetlocation):
            
            self.player.setPos(targetlocation)
        #print(direction.x, " ",  direction.y)
    
    def set_player_pos(self,pos):
        if not isinstance(pos,Vec2d):
            raise TypeError("map.set_player_pos only accepts vec2d")
        self.player.setPos(pos)

    def shortest_path_a_star(self,origin,goal):
        open_list = [origin]
        closed_list = []

        #path = (!(origin))

        while len(open_list) != 0:
            pass

    def shortest_path_bfs(self,startpos,goalpos):
        flooded_map = [[-1] * self.len.x] * self.len.y

        neighbour_queue = []

        neighbour_queue.append(startpos)

        for column in flooded_map:
            for x in column:
                if



    def __repr__(self) -> str:
        s = ""
        iy = 0
        for row in self.map:
            i = 0
            for column in row:
                if self.query_tile_collision(Vec2d(i,iy)):
                    s = s + "#"
                else:
                    s = s + "_"
                i+=1
            s = s+"\n"
            iy +=1
        return s

if __name__ == "__main__":
    map = Map("default")
    print(map)
    print(map.query_tile_textures(Vec2d(0,0)))