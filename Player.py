from math import sin, radians

MAX_POS = 400
MIN_POS = 0
MAX_VELOCITY = 10
MIN_VELOCITY = -10

PLAYER = 0

class Player:
    def __init__(self):
        self.position = (int((MAX_POS-MIN_POS)/2),int((MAX_POS-MIN_POS)/2))
        self.direction = 0 # 0-359
        self.velocity = (0,0)
        self.isAlive = True
        self.identity = PLAYER
    
    def move(self):
        newX, newY = self.position[0] + self.velocity[0], self.position[1] + self.velocity[1]
        if newX >= MAX_POS:  newX -= MAX_POS
        if newX < MIN_POS:   newX += MAX_POS
        if newY >= MAX_POS:  newY -= MAX_POS
        if newY < MIN_POS:   newY += MAX_POS
        self.position = (newX, newY)

    def changeVelocity(self, magnitude):
        newX = self.velocity[0] + magnitude * sin(radians(self.direction+180))
        newY = self.velocity[1] + magnitude * sin(radians(self.direction+270))
        if newX >= MAX_VELOCITY:  newX = MAX_VELOCITY
        if newX < MIN_VELOCITY:   newX = MIN_VELOCITY
        if newY >= MAX_VELOCITY:  newY = MAX_VELOCITY
        if newY < MIN_VELOCITY:   newY = MIN_VELOCITY
        self.velocity = (newX, newY)
    
    def changeDirection(self, value):
        newDir = value + self.direction
        if newDir >= 360: newDir -= 360
        if newDir < 0:    newDir += 360
        self.direction = newDir