from vec2d import Vec2d
from player import Player

class Map():
    
    
    def __init__(self) -> None:
        self.mapdata = [ [1,1,0,1],
            [1,0,0,1],
            [1,0,1,1],
            [1,0,1,1]]

        self.size = Vec2d(len(self.mapdata[0]),len(self.mapdata))
        self.player = Player(Vec2d(2,0))
         

    def __repr__(self) -> str:
        ss=""
        for row in self.mapdata:
            for col in row:
                if col:
                    ss = ss + "#"
                else:
                    ss = ss + " "
                
            ss = ss + "\n"
        return ss
    
    def load_map_from_file(self,mapfile):
        self.mapdata = mapfile