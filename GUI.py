import tkinter as tk
from PIL import ImageTk, Image  

PLAYER = 0
ASTROID = 1
MINI_ASTROID = 2
BULLET = 2

class GUI:
    def __init__(self, player):
        self.window = tk.Tk()
        self.window.title("Astroids")
        self.frame = tk.Frame(self.window)
        self.frame.pack()
        self.canvas = tk.Canvas(self.frame, width=400, height=400, background="black")
        self.canvas.pack()
        self.playerImg = Image.open("./images/player.png")
        self.astroidImg = Image.open("./images/astroid.png")
        self.miniAstroidImg = Image.open("./images/miniAstroid.png")
        self.bulletImg = Image.open("./images/bullet.png")
        self.arrowKeysImg = Image.open("./images/arrowKeys.png")
        self.player = player

    def update(self, board, score):
        self.canvas.delete('all')

        player = ImageTk.PhotoImage(self.playerImg.rotate(self.player.direction))
        astroid = ImageTk.PhotoImage(self.astroidImg)
        miniAstroid = ImageTk.PhotoImage(self.miniAstroidImg)
        bullet = ImageTk.PhotoImage(self.bulletImg)

        for object in board:
            if object.identity == PLAYER:
                self.canvas.create_image(object.position, image=player)
            if object.identity == ASTROID:
                if object.type == ASTROID:
                    self.canvas.create_image(object.position, image=astroid)
                if object.type == MINI_ASTROID:
                    self.canvas.create_image(object.position, image=miniAstroid)
            if object.identity == BULLET:
                self.canvas.create_image(object.position, image=bullet)
        
        self.canvas.create_text(340, 30, text="SCORE: {}".format(score), fill="white", font="Helvetica 10")

        self.window.update()
    
    def gameOver(self, score):
        self.canvas.create_text(200, 200, text="GAME OVER\nSCORE: {}".format(score), fill="white", font="Helvetica 20")
        self.window.update()

    def gameStart(self):
        arrowKeys = ImageTk.PhotoImage(self.arrowKeysImg)
        self.canvas.create_text(200, 100, text="ASTROIDS", fill="white", font="Helvetica 20")
        self.canvas.create_image((200, 200), image=arrowKeys)
        self.canvas.create_text(200, 300, text="UP and DOWN to accelerate\nLEFT and RIGHT to rotate\nSPACE to shoot", fill="white", font="Helvetica 16")
        self.window.update()


if __name__ == "__main__":
    gui = GUI()
    gui.window.mainloop()