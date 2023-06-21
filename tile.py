from vec2d import Vec2d
from PIL import Image, ImageTk

class Tile():
    
    
    def __init__(self,collide,image) -> None:
        if collide == None:
            collide = False
        elif not isinstance(collide,bool):
            raise TypeError("Tile() argument 1 only accepts bools")
        if image == None:
            image = Image.open("O:\\programming\\vscode\\csi-project\\13csi-project-SeanOPHagley\\default-floor.png").resize((self.Tile_size_x,self.Tile_size_y))
        elif not isinstance(image,bool):
            raise TypeError("Tile() argument 1 only accepts bools")
        
        self.collisions = collide
        self.image = image

