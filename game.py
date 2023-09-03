import os
import time
import tkinter as tk
import tkinter.messagebox

from PIL import Image, ImageTk

from map import Map
from vec2d import Vec2d


class Game:

    def __init__(self) -> None:

        self.flooded_map = None
        self.winlabel = None
        self.canvas = None
        self.userinput = False
        self.Map = Map("")
        self.images = []
        self.root = tk.Tk()



        self.menu = tk.Menu(self.root)

        self.mapmenu = tk.Menu(self.menu, tearoff=0)
        self.mapmenu.add_command(label="default", command=lambda: self.setmap(""))

        self.filemenu = tk.Menu(self.menu, tearoff=0)
        self.filemenu.add_cascade(label="Load Map", menu=self.mapmenu)
        self.filemenu.add_separator()

        self.filemenu.add_command(label="Exit", command=self.root.destroy)
        self.menu.add_cascade(label="File", menu=self.filemenu)

        self.helpmenu = tk.Menu(self.menu, tearoff=0)
        self.helpmenu.add_command(label="Controls", command= lambda: tkinter.messagebox.showinfo(title="Controls",message="- Use arrow keys to move\n"))
        self.helpmenu.add_command(label="Game", command=lambda: tkinter.messagebox.showinfo(title="Game",message="- To win you have to get to the goal.\n- To change mazes you can use the file menu -> load map."))
        self.helpmenu.add_command(label="Shortest Path",command= self.shortest_path_flood_fill)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)

        self.setmap("")

        for path in self.Map.texture_paths:
            self.images.append(
                ImageTk.PhotoImage(Image.open(path).resize([self.Map.tile_size, self.Map.tile_size], Image.NEAREST)))

        #self.refreshmaplist()

        self.root.config(menu=self.menu)

    def loadmap(self):
        self.setmap("")
        pass

    def refreshmaplist(self):

        self.mapmenu.delete(0, "end")

        self.mapmenu.add_command(label="default", command=lambda: self.setmap(""))
        self.mapmenu.add_separator()

        for m in os.listdir("./maps/"):
            #print(m)
            if m != "default":
                #print("m is not default, it's " + m + "!")
                a = m
                self.mapmenu.add_command(label=a, command=lambda: self.setmap(a))
        #self.filemenu.add_cascade(label="Load Map", menu=self.mapmenu)

    def setmap(self, mapname) -> None:
        self.Map = Map(mapname)
        self.images = []
        # self.root = tk.Tk()

        #self.refreshmaplist()
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
            self.images.append(
                ImageTk.PhotoImage(Image.open(path).resize([self.Map.tile_size, self.Map.tile_size], Image.NEAREST)))

        self.flooded_map = self.Map.map_flood_fill(self.Map.player.position,self.Map.goal)

        self.__rendermaze()
        self.userinput = True
        self.refreshmaplist()

    def __rendermaze(self) -> None:
        self.canvas.delete()
        iy = 0
        for y in self.Map.map:
            ix = 0
            for x in y:
                x_size = ix * self.Map.tile_size + self.Map.tile_size / 2
                y_size = iy * self.Map.tile_size + self.Map.tile_size / 2
                x_pos = ix * self.Map.tile_size + self.Map.tile_size / 2
                y_pos = iy * self.Map.tile_size + self.Map.tile_size / 2
                # cell_textures = self.Map.map[y][x]
                # print(x_pos)
                # print(y_pos)
                for texture in x:
                    # print(texture)
                    # print(self.Map.textures[texture[0]])
                    # image = ImageTk.PhotoImage(self.images[texture[0]])
                    image = self.images[texture[0]]
                    # print(image)
                    # print(self.Map.textures[texture[0]])
                    self.canvas.create_image(x_pos, y_pos, image=image)
                ix += 1
            iy += 1

        x_pos = self.Map.player.position.x * self.Map.tile_size + self.Map.tile_size / 2
        y_pos = self.Map.player.position.y * self.Map.tile_size + self.Map.tile_size / 2

        self.PlayerImage = self.canvas.create_image(x_pos, y_pos, image=self.images[self.Map.player.texture])

    def update_player_image(self):
        # print("u")
        self.canvas.moveto(self.PlayerImage,
                           self.Map.player.position.x * self.Map.tile_size,
                           self.Map.player.position.y * self.Map.tile_size,
                           )

    def win(self):
        print("win")
        self.userinput = False
        self.winlabel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def shortest_path_flood_fill(self):
        current_distance = self.flooded_map[self.Map.player.position.y][self.Map.player.position.x]
        while self.Map.player.position is not self.Map.goal:
            player_pos = self.Map.player.position
            if player_pos.y + 1 < len(self.flooded_map) and self.flooded_map[player_pos.y + 1][player_pos.x] != -1 and self.flooded_map[player_pos.y + 1][player_pos.x] < current_distance:
                current_distance = self.flooded_map[player_pos.y + 1][player_pos.x]
                self.mov(Vec2d(0,1))
                print("Down")
            elif player_pos.y - 1 >= 0 and self.flooded_map[player_pos.y - 1][player_pos.x] != -1 and self.flooded_map[player_pos.y - 1][player_pos.x] < current_distance:
                current_distance = self.flooded_map[player_pos.y - 1][player_pos.x]
                self.mov(Vec2d(0,-1))
                print("Up")
            elif player_pos.x + 1 < len(self.flooded_map[player_pos.y]) and self.flooded_map[player_pos.y][player_pos.x + 1] != -1 and self.flooded_map[player_pos.y][player_pos.x + 1] < current_distance:
                current_distance = self.flooded_map[player_pos.y][player_pos.x + 1]
                self.mov(Vec2d(1,0))
                print("Right")
            elif player_pos.x - 1 >= 0 and self.flooded_map[player_pos.y][player_pos.x - 1] != -1 and self.flooded_map[player_pos.y][player_pos.x - 1] < current_distance:
                current_distance = self.flooded_map[player_pos.y][player_pos.x - 1]
                self.mov(Vec2d(-1,0))
                print("Left")
            else:
                print("Break")
                break
            self.root.update()
            #self.root.after(ms=1 ,func=self.shortest_path_flood_fill)
            time.sleep(0.1)

    def mov(self, d):
        self.Map.move_player(d)
        self.update_player_image()
        if self.Map.player.position.x == self.Map.goal.x and self.Map.player.position.y == self.Map.goal.y:
            self.win()

    def up(self, e):
        if not self.userinput:
            return
        self.mov(Vec2d(0, -1))

    def down(self, e):
        if not self.userinput:
            return
        self.mov(Vec2d(0, 1))

    def left(self, e):
        if not self.userinput:
            return
        self.mov(Vec2d(-1, 0))

    def right(self, e):
        if not self.userinput:
            return
        self.mov(Vec2d(1, 0))

    def run(self):
        # self.__renderMaze()
        self.root.bind('<Up>', self.up)
        self.root.bind('<Down>', self.down)
        self.root.bind('<Left>', self.left)
        self.root.bind('<Right>', self.right)
        self.root.mainloop()


if __name__ == "__main__":
    g = Game()
    g.setmap("default")
    g.rendermaze()
    g.run()
