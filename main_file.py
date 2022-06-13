import time
import turtle
from snake_class import *
from food import *
from score_board import *

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("my snake game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

game_is_on = True

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while game_is_on:
      
    #screen.update()
    time.sleep(0.1)
    screen.update() # It's advisable to keep updating the screen in a loop
            
    snake.move()

    # detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.extend_snake()

    # detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset_score()
        game_is_on = False
        score_board.game_over()
    
    # detect collision with body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
           score_board.reset_score()
           game_is_on = False
           score_board.game_over()
        
    
screen.exitonclick()