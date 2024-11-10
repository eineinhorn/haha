import pygame
from pygame.locals import *

pygame.init()
pygame.joystick.init()

screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("Input Display")

joy = pygame.joystick.Joystick(0)

class Button:
    def __init__(self, axis=False, id=0, color=(50,50,50), circle=True, x=0, y=0):
        if not axis:
            self.button = joy.get_button(id)
        if axis:
            self.button = joy.get_axis(id)
        self.color = color
        self.x, self.y = x, y
        self.circle = circle
        if self.circle:
            self.form = pygame.draw.circle(screen, self.color, (self.x, self.y), 20)
        else:
            self.form = pygame.draw.rect(screen, self.color, (self.x, self.y, 40, 40))
    
    def draw(self):
        if self.circle:
            self.form = pygame.draw.circle(screen, self.color, (self.x, self.y), 20)
        else:
            self.form = pygame.draw.rect(screen, self.color, (self.x, self.y, 40, 40))
            
class Axis:
    def __init__(self, idx=0, idy=0, color=(0,0,0), x=0, y=0):
        self.color = color
        self.x, self.y = x, y
        self.axis = joy.get_axis(idx)
        self.ayis = joy.get_axis(idy)

    def draw(self):
        self.x += self.axis*30
        self.y += self.ayis*30
        self.form = pygame.draw.circle(screen, self.color, (self.x, self.y), 30)
        
        

run = True
while run:
    screen.fill((125,125,125))
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    
    Cross = Button(id=0, x=400, y=200)
    Circle = Button(id=1, x=450, y=150)
    Square = Button(id=2, x=350, y=150)
    Triangle = Button(id=3, x=400, y=100)
    Share = Button(id=4, circle=False, x=225, y=55)
    Options = Button(id=6, circle=False, x=275, y=55)
    TLeft = Button(id=9, circle=False, x=0, y=50)
    TRight = Button(id=10, circle=False, x=460, y=50)
    Up = Button(id=11, circle=False, x=100, y=100)
    Down = Button(id=12, circle=False, x=100, y=200)
    Left = Button(id=13, circle=False, x=50, y=150)
    Right = Button(id=14, circle=False, x=150, y=150)
    AxLeft = Button(axis=True, id=4, circle=False, x=0, y=0)
    AxRight = Button(axis=True, id=5, circle=False, x=460, y=0)
    
    LeftStick = Axis(idx=0, idy=1, x=100, y=300)
    if joy.get_button(7):
        LeftStick.color = (255,255,255)
    else:
        LeftStick.color = (0,0,0)
    LeftStick.draw()
    
    RightStick = Axis(idx=2, idy=3, x=400, y=300)
    if joy.get_button(8):
        RightStick.color = (255,255,255)
    else:
        RightStick.color = (0,0,0)
    RightStick.draw()
    
    buttons = [Cross, Circle, Square, Triangle, Share, Options, TLeft, TRight, Up, Down, Left, Right, AxLeft, AxRight]
    for button in buttons:
        if button.button > 0:
            button.color = (255,255,255)
        else:
            button.color = (50,50,50)
        button.draw()
    
    pygame.display.flip()
