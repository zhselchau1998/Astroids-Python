from math import sin, radians

SPEED = 19
MAX_POS = 400
MIN_POS = 0

BULLET = 2

class Bullet:
    def __init__(self, position, direction):
        self.velocity = (SPEED * sin(radians(direction+180)), SPEED * sin(radians(direction+270)))
        self.position = position
        self.isAlive = True
        self.identity = BULLET

    def move(self):
        newX, newY = self.position[0] + self.velocity[0], self.position[1] + self.velocity[1]
        if newX >= MAX_POS:  self.isAlive = False
        if newX < MIN_POS:   self.isAlive = False
        if newX >= MAX_POS:  self.isAlive = False
        if newX < MIN_POS:   self.isAlive = False
        self.position = (newX, newY)