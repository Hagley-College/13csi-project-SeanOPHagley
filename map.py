from vec2d import Vec2d

class Map():
    map = [ [1,1,0,1],
            [1,0,0,1],
            [1,0,1,1],
            [1,0,1,1]]
    
    def __init__(self) -> None:
        self.x = map#[]
        self.spawn = Vec2d(2,0)
        

    def __repr__(self) -> str:
        ss=""
        for row in self.map:
            for col in row:
                if col:
                    ss = ss + "#"
                else:
                    ss = ss + " "
                
            ss = ss + "\n"
        return ss
    
    def load_map_from_file(self,mapfile):
        self.map = mapfile