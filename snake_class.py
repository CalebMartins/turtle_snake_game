import turtle
import random

turtle.colormode(255)
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_sake()
        self.head = self.segments[0]

    def create_sake(self):
        """creates the snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)
           
    
    def add_segment(self, position: tuple):
        '''adds segment to the sake when it collides with food'''
        snake = turtle.Turtle(shape='square')
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        snake.color((r, g, b))
        # snake.speed('fastest')
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)
    
    def extend_snake(self):
        """extends length of food when it collides with food"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """moves the snake in the direction it's facing"""
        
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor() 
            new_y = self.segments[segment - 1].ycor() 
            self.segments[segment].goto(new_x, new_y)
            
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        """turns snake in the direction of the up arrow key"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    
    def down(self):
        """turns snake in the direction of the down arrow key"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        """turns snake in the direction of the left arrow key"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        """turns snake in the direction of the right arrow key"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    

    


# snake = Snake()
# print(snake.segments)