import tkinter as tk
from PIL import Image, ImageTk
from game import Game

gameobj = Game()
  
gameobj.set_tile_size(32)

gameobj.render()
gameobj.root.mainloop()


# C:\WPy64-3870\python-3.8.7.amd64\python.exe5