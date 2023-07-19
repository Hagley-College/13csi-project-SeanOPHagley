import tkinter as tk
from PIL import Image, ImageTk

from map import Map
from vec2d import Vec2d

class Game:
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
        self.canvas.delete()
        for path in self.Map.texture_paths:
            self.images.append(ImageTk.PhotoImage(Image.open(path).resize([self.Map.tile_size,self.Map.tile_size],Image.NEAREST)))
        #self.canvas = tk.Canvas(self.root, width=self.Map.canvas_size[0], height=self.Map.canvas_size[1])
        print(self.Map.canvas_size)
        self.canvas.pack()

    def __renderMaze(self) -> None:
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
        
        x_pos = self.Map.player.position.x * self.Map.tile_size + self.Map.tile_size/2
        y_pos = self.Map.player.position.y * self.Map.tile_size + self.Map.tile_size/2

        self.PlayerImage = self.canvas.create_image(x_pos, y_pos, image=self.images[self.Map.player.texture])
        
    def update_player_image(self):
        #print("u")
        self.canvas.moveto(self.PlayerImage,
                         self.Map.player.position.x * self.Map.tile_size,
                         self.Map.player.position.y * self.Map.tile_size,
)
        
    def up(self,e):
        print("up")
        self.Map.move_player(Vec2d(0,-1))
        self.update_player_image()
        print(self.Map.player.position)

    def down(self,e):
        print("down")
        self.Map.move_player(Vec2d(0, 1))
        self.update_player_image()
        print(self.Map.player.position)

    def left(self,e):
        print("left")
        self.Map.move_player(Vec2d(-1, 0))
        self.update_player_image()
        print(self.Map.player.position)

    def right(self,e):
        print("right")
        self.Map.move_player(Vec2d(1, 0))
        self.update_player_image()
        print(self.Map.player.position)

        
    def run(self):
        self.__renderMaze()
        self.root.bind('<Up>', self.up)
        self.root.bind('<Down>', self.down)
        self.root.bind('<Left>', self.left)
        self.root.bind('<Right>', self.right)
        self.root.mainloop()
        
        

if __name__ == "__main__":
    g = Game()
    g.setMap("default")
    g.renderMaze()
    g.run()