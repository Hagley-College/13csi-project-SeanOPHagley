class Vec2d:
    def __init__(self,x,y) -> None:
        # Check correct types
        if not (isinstance(x,int) or isinstance(x,float)):
            raise TypeError("vec2d.x must be a number")
        if not (isinstance(y,int) or isinstance(y,float)):
            raise TypeError("vec2d.y must be a number")
        self.x = x
        self.y = y
    
    def __add__(self,b):
        if not isinstance(b,Vec2d):
            raise TypeError("Vec2d.__add__ can only do arithmetic with other Vec2d classes.")
        result = Vec2d(self.x+b.x,self.y+b.y)
        return result

    def __repr__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ")"
