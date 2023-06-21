import tkinter as tk
from PIL import Image, ImageTk

from map import Map
from vec2d import Vec2d
from player import Player

class Game:
    def __init__(self) -> None:

        # Defaults
        self.Map = Map()
        self.yLen = self.Map.size.y
        self.xLen = self.Map.size.x
        self.Tile_size_x = 50
        self.Tile_size_y = 50
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=640, height=480)
        self.canvas.pack()
        self.Wall_texture = ImageTk.PhotoImage(Image.open("O:\\programming\\vscode\\csi-project\\13csi-project-SeanOPHagley\\default-wall.png").resize((self.Tile_size_x,self.Tile_size_y)))
        self.Floor_texture = ImageTk.PhotoImage(Image.open("O:\\programming\\vscode\\csi-project\\13csi-project-SeanOPHagley\\default-floor.png").resize((self.Tile_size_x,self.Tile_size_y)))
        self.Player_texture = ImageTk.PhotoImage(Image.open("O:\\programming\\vscode\\csi-project\\13csi-project-SeanOPHagley\\default-floor.png").resize((self.Tile_size_x,self.Tile_size_y)))
        self.Player = Player()


    def set_tile_size(self,size):

        # Type checking
        if isinstance(size,Vec2d):
            self.Tile_size_x = Vec2d.x
            self.Tile_size_y = Vec2d.y

        elif isinstance(size,int):
            self.Tile_size_x = size
            self.Tile_size_y = size

        elif isinstance(size,float):
            self.Tile_size_x = size
            self.Tile_size_y = size
        else:
            raise TypeError("Game.set_tile_size() only accepts Vec2d, int or float")
        self.Wall_texture = ImageTk.PhotoImage(Image.open("O:\\programming\\vscode\\csi-project\\13csi-project-SeanOPHagley\\default-wall.png").resize((self.Tile_size_x,self.Tile_size_y)))
        self.Floor_texture = ImageTk.PhotoImage(Image.open("O:\\programming\\vscode\\csi-project\\13csi-project-SeanOPHagley\\default-floor.png").resize((self.Tile_size_x,self.Tile_size_y)))
        
        # Resize textures to match tile size
        #self.Wall_texture.resize([self.Tile_size_x,self.Tile_size_y])
        #self.Floor_texture.resize([self.Tile_size_x,self.Tile_size_y])

    def setPlayerPos(self,pos):
        if not isinstance(pos,Vec2d):
            raise TypeError("setPlayerPos() only accepts Vec2d as argument.")
        self.Player.position = pos
        
    def setImagePos(self,pos):
        if not isinstance(pos,Vec2d):
            raise TypeError("setImagePos() only accepts Vec2d as argument.")
        

    def load_map(self,mapfile):
        self.map = Map()
        #self.map.load_map_from_file(mapfile)


    # TODO load map properly
    def render(self):
        self.canvas.delete()

        for iX in range(self.Map.size.x):
            for iY in range(self.Map.size.y):
                image = self.Floor_texture
                if self.Map.mapdata[iY][iX]:
                    image = self.Wall_texture

                self.canvas.create_image(iX * self.Tile_size_x + self.Tile_size_x/2, iY * self.Tile_size_y + self.Tile_size_y/2, image=image)
        
            

        # for row in range(self.rows):
        #     for col in range(self.cols):
        #         #Note when creating an image it will appear with the center of the image at the coordinate x, y.
        #         x = col * self.cell_size + self.cell_size//2
        #         y = row * self.cell_size + self.cell_size//2
        #         cell_type = self.maze[row][col]
        #         image = self.images[cell_type]
        #         self.canvas.create_image(x, y, image=image)
        # #self.canvas.create_rectangle(50,100,150,150,fill="red")
        # image= self.images["agent"]
        # x = 1 * self.cell_size + self.cell_size//2
        # y = 0 * self.cell_size + self.cell_size//2
        # self.canvas.create_image(x, y, image=image)

        # print("Unimplemented")
