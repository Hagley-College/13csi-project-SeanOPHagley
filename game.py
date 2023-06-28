import tkinter as tk
from PIL import Image, ImageTk

from map import Map
from vec2d import Vec2d

class Game():
    def __init__(self) -> None:
        self.Map = Map("")
        self.images = []
        self.root = tk.Tk()
        for path in self.Map.texture_paths:
            self.images.append(ImageTk.PhotoImage(Image.open(path).resize([self.Map.tile_size,self.Map.tile_size],Image.NEAREST)))
        self.canvas = tk.Canvas(self.root, width=self.Map.canvas_size[0], height=self.Map.canvas_size[1])
        self.canvas.pack()
        
    def setMap(self,mapname) -> None:
        self.Map = Map(mapname)
        self.images = []
        #self.root = tk.Tk()
        for path in self.Map.texture_paths:
            self.images.append(ImageTk.PhotoImage(Image.open(path).resize([self.Map.tile_size,self.Map.tile_size],Image.NEAREST)))
        self.canvas = tk.Canvas(self.root, width=self.Map.canvas_size[0], height=self.Map.canvas_size[1])
        print(self.Map.canvas_size)
        self.canvas.pack()

    def renderMaze(self) -> None:
        self.canvas.delete()
        iy = 0
        for y in self.Map.map:
            ix = 0
            for x in y:
                x_size = ix * self.Map.tile_size + self.Map.tile_size/2
                y_size = iy * self.Map.tile_size + self.Map.tile_size/2
                x_pos = ix * self.Map.tile_size + self.Map.tile_size/2
                y_pos = iy * self.Map.tile_size + self.Map.tile_size/2
                #cell_textures = self.Map.map[y][x]
                print(x_pos)
                print(y_pos)
                for texture in x:
                    #print(texture)
                   # print(self.Map.textures[texture[0]])
                    #image = ImageTk.PhotoImage(self.images[texture[0]])
                    image = self.images[texture[0]]
                    #print(image)
                    #print(self.Map.textures[texture[0]])
                    self.canvas.create_image(x_pos, y_pos, image=image)
                ix += 1
            iy += 1
                
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    g = Game()
    g.setMap("default")
    g.renderMaze()
    g.run()