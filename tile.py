from vec2d import Vec2d
from PIL import Image, ImageTk

class Tile():
    
    
    def __init__(self,collide,image) -> None:
        if collide == None:
            collide = False
        elif not isinstance(collide,bool):
            raise TypeError("Tile() argument 1 only accepts bools")
        
        if not isinstance(image,int):
            raise TypeError("Tile() argument 2 only accepts numbers")
        
        self.collisions = collide
        self.image = image

