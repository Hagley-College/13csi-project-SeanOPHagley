import tkinter as tk
from PIL import Image, ImageTk

from map import Map
from vec2d import Vec2d

class Game():
    def __init__(self) -> None:
        self.Map = Map("")

        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=self.Map.canvas_size[0], height=self.Map.canvas_size[1])
        self.canvas.pack()
        pass

    def setMap(self,mapname) -> None:
        self.Map = Map(mapname)
        self.root = tk.Tk
        self.canvas = tk.Canvas(self.root, width=self.Map.canvas_size[0], height=self.Map.canvas_size[1])

    def renderMaze(self) -> None:
        self.canvas.delete()
        pass