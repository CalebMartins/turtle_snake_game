from  turtle import *
import json
FILENAME = "snake_game.json"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.goto(0, 270)
        self.pencolor("white")
        self.score = 0
        self.saved_high_score = 0
        self.update_score()
    
    def update_score(self):
        """updates score"""
        self.clear()
        try:
            with open(FILENAME) as f:
                self.saved_high_score = json.load(f)
        except FileNotFoundError:
            pass
        
        self.write(f"score: {self.score}  High Score: {self.saved_high_score}", align='center', font=('arial', 15, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()


    def reset_score(self):
        if self.score > self.saved_high_score:
            self.saved_high_score = self.score
            self.store_high_score(self.saved_high_score)
        
        self.score = 0
        self.update_score()
    
    def store_high_score(self, high_score):
        """stores high score"""
        with open(FILENAME, 'w') as f:
            json.dump(high_score, f)
        
    def game_over(self):
        """prints gameover when theres a collision with the wall"""
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=('arial', 10, 'normal'))   

# c = ScoreBoard()
# c.reset_score()
