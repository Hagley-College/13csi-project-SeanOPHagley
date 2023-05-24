import tkinter as tk
from PIL import Image, ImageTk
from game import Game

gameobj = Game()

gameobj.set_tile_size(11)

gameobj.render()
gameobj.root.mainloop()