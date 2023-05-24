import tkinter as tk
from PIL import Image, ImageTk

class MazeGame:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.cell_size = 50
        self.canvas_width = self.cols * self.cell_size
        self.canvas_height = self.rows * self.cell_size

        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.images = {
            0: ImageTk.PhotoImage(Image.open("//Amazon2/sean.ogdenprice$/Downloads/MicrosoftTeams-image.png").resize((self.cell_size, self.cell_size))),
            1: ImageTk.PhotoImage(Image.open("//Amazon2/sean.ogdenprice$/Downloads/MicrosoftTeams-image (1).png").resize((self.cell_size, self.cell_size))),
            "agent": ImageTk.PhotoImage(Image.open("//Amazon2/sean.ogdenprice$/Downloads/MicrosoftTeams-image (2).png").resize((self.cell_size, self.cell_size)))
        }

        self.draw_maze()

    def draw_maze(self):
        self.canvas.delete()
        for row in range(self.rows):
            for col in range(self.cols):
                #Note when creating an image it will appear with the center of the image at the coordinate x, y.
                x = col * self.cell_size + self.cell_size//2
                y = row * self.cell_size + self.cell_size//2
                cell_type = self.maze[row][col]
                image = self.images[cell_type]
                self.canvas.create_image(x, y, image=image)
        #self.canvas.create_rectangle(50,100,150,150,fill="red")
        image= self.images["agent"]
        x = 1 * self.cell_size + self.cell_size//2
        y = 0 * self.cell_size + self.cell_size//2
        self.canvas.create_image(x, y, image=image)


    def run(self):
        self.root.mainloop()

# Example usage
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

game = MazeGame(maze)
game.run()
