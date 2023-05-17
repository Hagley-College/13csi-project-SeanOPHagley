import sys

class Player():
    x = 0
    y = 0

    def init(self,X,Y):
        self.x = X
        self.y = Y


    # Direction 1 is for right, -1 for left, 2 for up, -2 for down
    def move(self, direction):
        if direction == 1: # Right
            self.x += 1
        elif direction == -1: # Left
            self.x += -1
        elif direction == 2: # Up
            self.y += -1
        elif direction == -2: # Down
            self.y += 1

    def setPos(self,setx,sety):
        self.x = setx
        self.y = sety

    def __repr__(self):
        return f"x:{self.x}, y:{self.y}"
    