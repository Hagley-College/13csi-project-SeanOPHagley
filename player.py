import sys
from vec2d import Vec2d

class Player():
    

    def init(self,pos):
        if pos == None:
            pos = Vec2d(0,0)
        elif not isinstance(pos,Vec2d):
            raise TypeError("Player() only accepts Vec2d")
        self.position = pos


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

    def setPos(self,setx,sety):
        self.x = setx
        self.y = sety

    def __repr__(self):
        return f"x:{self.x}, y:{self.y}"
    