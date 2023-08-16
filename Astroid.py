from random import randint


MAX_VELOCITY = 5
MIN_VELOCITY = -5
MAX_POS = 400
MIN_POS = 0

ASTROID = 1
MINI_ASTROID = 2

class Astroid:
    def __init__(self, size:int, type=ASTROID, position = (0,0)):
        self.size = size
        self.velocity = (randint(MIN_VELOCITY,MAX_VELOCITY+1), randint(MIN_VELOCITY,MAX_VELOCITY+1))
        if self.velocity == (0,0): self.velocity = (1,1)
        tmp = randint(0,4)
        self.position = position
        if self.position == (0,0):
            if tmp == 0:
                self.position = (randint(MIN_POS, MAX_POS), MAX_POS)
            if tmp == 1:
                self.position = (randint(MIN_POS, MAX_POS), MIN_POS)
            if tmp == 2:
                self.position = (MIN_POS, randint(MIN_POS, MAX_POS))
            if tmp == 3:
                self.position = (MAX_POS, randint(MIN_POS, MAX_POS))
        self.isAlive = True
        self.identity = ASTROID
        self.type = type

    def move(self):
        newX, newY = self.position[0] + self.velocity[0], self.position[1] + self.velocity[1]
        if newX >= MAX_POS:  newX -= MAX_POS
        if newX <  MIN_POS:  newX += MAX_POS
        if newY >= MAX_POS:  newY -= MAX_POS
        if newY <  MIN_POS:  newY += MAX_POS
        self.position = (newX, newY)
    
    def overlaps(self, position)->bool:
        xDiff, yDiff = position[0] - self.position[0], position[1] - self.position[1]

        if xDiff >= -self.size/2 and xDiff < self.size/2 and yDiff >= -self.size/2 and yDiff < self.size/2:
            return True
        return False


    