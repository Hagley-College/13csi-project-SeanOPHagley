import tkinter as tk
from PIL import Image, ImageTk

from map import Map
from vec2d import Vec2d

class Game:
    def __init__(self) -> None:
        
        self.images = []
        self.root = tk.Tk()
        self.setMap("")
        for path in self.Map.texture_paths:
            self.images.append(ImageTk.PhotoImage(Image.open(path).resize([self.Map.tile_size,self.Map.tile_size],Image.NEAREST)))
        
        #self.canvas = tk.Canvas(self.root, width=self.Map.canvas_size[0], height=self.Map.canvas_size[1])
        #self.canvas.pack()
        self.menu = tk.Menu(self.root)

        self.mapmenu = tk.Menu(self.menu,tearoff=0)
        self.mapmenu.add_command(label="default",command=self.loadMap)

        self.filemenu = tk.Menu(self.menu,tearoff=0)
        self.filemenu.add_cascade(label="Load Map",menu=self.mapmenu)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command=self.root.destroy)
        self.menu.add_cascade(label="File",menu=self.filemenu)

        self.helpmenu = tk.Menu(self.menu,tearoff=0)
        self.helpmenu.add_command(label="Controls")
        self.menu.add_cascade(label="Help",menu=self.helpmenu)
        

        
        #self.userinput = True

        self.root.config(menu=self.menu)

    def loadMap(self):
        self.setMap("")
        pass

    def setMap(self,mapname) -> None:
        self.Map = Map(mapname)
        self.images = []
        #self.root = tk.Tk()


        try:
            self.canvas.delete()
            self.canvas.config(width=self.Map.canvas_size[0], height=self.Map.canvas_size[1])
        except:
            self.canvas = tk.Canvas(self.root, width=self.Map.canvas_size[0], height=self.Map.canvas_size[1])
            self.canvas.pack()

        try:
            self.winlabel.place_forget()
        except:
            self.winlabel = tk.Label(self.root, text="You win")
            self.winlabel.place_forget()

        for path in self.Map.texture_paths:
            self.images.append(ImageTk.PhotoImage(Image.open(path).resize([self.Map.tile_size,self.Map.tile_size],Image.NEAREST)))
        #self.canvas = tk.Canvas(self.root, width=self.Map.canvas_size[0], height=self.Map.canvas_size[1])
        
        #print(self.Map.canvas_size)
        self.__renderMaze()
        self.userinput = True
        #self.winlabel.grid_remove()

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
                #print(x_pos)
                #print(y_pos)
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

    def win(self):
        print("win")
        #txt = tk.Text(self.root, height=16,width =64)
        #lbl = tk.Label(self.root, text="Winner!")
        #lbl.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.userinput = False
        self.winlabel.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

    def mov(self, d):
        self.Map.move_player(d)
        self.update_player_image()
        if self.Map.player.position.x == self.Map.goal.x and self.Map.player.position.y == self.Map.goal.y:
            self.win()
    def up(self, e):
        if self.userinput == False:
            return
        self.mov(Vec2d(0, -1))

    def down(self, e):
        if self.userinput == False:
            return
        self.mov(Vec2d(0, 1))

    def left(self, e):
        if self.userinput == False:
            return
        self.mov(Vec2d(-1, 0))

    def right(self, e):
        if self.userinput == False:
            return
        self.mov(Vec2d(1, 0))

        
    def run(self):
        #self.__renderMaze()
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