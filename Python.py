import pygame
import math

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Slither")
clock = pygame.time.Clock()

xPos = 0
yPos = 0
xVelocity = 0
yVelocity = 0
mousePos = (0, 0)
totalVelocity = 2
totalDistance = 1 #This is to avoid a dividing by 0 error

doExit = False

class Segment:
    def __init__(self, color):
        self.x = 0
        self.y = 0
        self.xVelocity = 0
        self.yVelocity = 0
        self.color = color
        self.size = 5
        self.totalVelocity = 2
    
    def Move(self, position):
        self.distance = (position[0] - self.x, position[1] - self.x)
        self.totalDistance = (abs(self.distance[0]) + abs(self.distance[1]))

        if self.totalDistance == 0: self.totalDistance = 1

        self.xDir = round((self.distance[0]/self.totalDistance) * self.totalVelocity, 2)
        self.yDir = round((self.distance[1]/self.totalDistance) * self.totalVelocity, 2)

        self.step = 0.1

        self.xDiff = self.xDir - self.xVelocity
        self.yDiff = self.yDir - self.yVelocity

        if abs(self.xDiff) > self.step:
            self.xVelocity += self.step if self.xDiff > 0 else -self.step
        else:
            self.xVelocity = self.xDir

        if abs(self.yDiff) > self.step:
            self.yVelocity += self.step if self.yDiff > 0 else -self.step
        else:
            self.yVelocity = self.yDir


        self.yVelocity = round((self.distance[1]/self.totalDistance) * self.totalVelocity, 2)
        self.x += self.xVelocity
        self.y += self.yVelocity

    def Draw(self): pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
    def GetCoords(self): return (self.x, self.y)
    def GetColor(self): return self.color


class Head(Segment):
    pass

class Tail(Segment):
    def __init__(self, following):
        self.following = following
        super().__init__(following.GetColor())

    def Move(self):
        if counter == 

snake = [Head((255,255,255))]
snake.append(Tail(snake[0]))
while not doExit:

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos

    snake[0].Move(mousePos)
    snake[1].Move()

    screen.fill((0,0,0))
    snake[0].Draw()
    snake[1].Draw()
    pygame.display.flip()

    

pygame.quit()