import sys
from vec2d import Vec2d

class Player():
    

    def __init__(self,pos,texture):
        if pos == None:
            pos = Vec2d(0,0)
        elif not isinstance(pos,Vec2d):
            raise TypeError("Player() argument 1 only accepts Vec2d")
        if texture == None:
            texture = 0
        elif not isinstance(texture,int):
            raise TypeError("Player() argument 2 only accepts int")
        self.position = pos
        self.texture = texture


    # Direction 1 is for right, -1 for left, 2 for up, -2 for down
    def move(self, direction):
        if direction == 1: # Right
            self.position.x += 1
        elif direction == -1: # Left
            self.position.x += -1
        elif direction == 2: # Up
            self.position.y += -1
        elif direction == -2: # Down
            self.position.y += 1

    def setPos(self,pos):
        if not isinstance(pos,Vec2d):
            raise TypeError("Player.setPos() only accepts Vec2d")
        
        self.position.x = pos
        self.position.y = pos

    def __repr__(self):
        return f"x:{self.position.x}, y:{self.position.y}, texture:{self.texture}"
    