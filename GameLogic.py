from Astroid import Astroid
from Player import Player
from Bullet import Bullet
from KeyListener import KeyListener
from time import sleep
from GUI import GUI

ACCELERATION = 1
ROTATION = 15

MAX_ASTROIDS = 4
ASTROID_SIZE = 20
MINI_ASTROID_SIZE = 10

PLAYER = 0
ASTROID = 1
MINI_ASTROID = 2
BULLET = 2

def deleteDeadObjects(listOfObjects:list)->list:
    return [obj for obj in listOfObjects if obj.isAlive]
        

class GameLogic:
    def __init__(self):
        self.inGame = True
        self.player = Player()
        self.keyboard = KeyListener()
        self.playerObjects = [self.player]
        self.astroidObjects = []
        self.score = 0
        self.maxAstroids = MAX_ASTROIDS
    
    def controlPlayer(self):
        keys = self.keyboard.getKeys()
        magnitude = 0
        rotation = 0

        if 'w' in keys: magnitude += ACCELERATION
        if 'a' in keys: rotation += ROTATION
        if 's' in keys: magnitude -= ACCELERATION
        if 'd' in keys: rotation -= ROTATION

        self.player.changeDirection(rotation)
        self.player.changeVelocity(magnitude)

        if 'space' in keys:
            self.playerObjects.append(Bullet(self.player.position, self.player.direction))

    def printPlayerInfo(self):
        print("\n")
        print("player position: {}".format(self.player.position))
        print("player velocity: {}".format(self.player.velocity))
        print("player rotation: {}".format(self.player.velocity))
        print(self.keyboard.getKeys())

    def startLoop(self):
        gui = GUI(self.player)
        i=0
        gui.gameStart()
        sleep(3)
        while self.player.isAlive:
            if i >= 1:
                self.controlPlayer()
                for obj in self.playerObjects+self.astroidObjects:
                    obj.move()
                #self.printPlayerInfo()

                while len(self.astroidObjects) < self.maxAstroids:
                    self.astroidObjects.append(Astroid(ASTROID_SIZE))

                self.playerObjects = deleteDeadObjects(self.playerObjects)
                self.astroidObjects = deleteDeadObjects(self.astroidObjects)
                for astroid in self.astroidObjects:
                    for obj in self.playerObjects:
                        if astroid.overlaps(obj.position):
                            astroid.isAlive = False
                            obj.isAlive = False
                            self.score += 100
                            if astroid.type == ASTROID:
                                self.astroidObjects.append(Astroid(MINI_ASTROID_SIZE, MINI_ASTROID, astroid.position))
                                self.astroidObjects.append(Astroid(MINI_ASTROID_SIZE, MINI_ASTROID, astroid.position))
                
                if self.maxAstroids < self.score / 500:
                    self.maxAstroids = self.score / 500

            i+=1
            gui.update(self.playerObjects + self.astroidObjects, self.score)
            sleep(0.1)
        gui.gameOver(self.score)
        sleep(3)

    def run(self):
        self.startLoop()