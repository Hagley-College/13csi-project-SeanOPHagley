class Vec2d:
    def __init__(self,x,y) -> None:
        # Check correct types
        if not (isinstance(x,int) or isinstance(x,float)):
            raise TypeError("vec2d.x must be a number")
        elif not (isinstance(y,int) or isinstance(y,float)):
            raise TypeError("vec2d.y must be a number")
        self.x = x
        self.y = y
    
    def add(self,b):
        result = Vec2d()
        result.x = self.x + b.x
        result.y = self.y + b.y
        return result