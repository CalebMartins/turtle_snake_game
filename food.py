import random
from turtle import *

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()
        
    def refresh(self):
        '''changes location of food'''
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)
    
