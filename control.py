import random
from ball import Ball
from setup import Paddle
from turtle import Screen
from score_board import ScoreBoard
PADDLE_DISTANCE = 6
STOP = 0


class Control(Ball):
    def __init__(self):
        super().__init__()
        self.horizontal_wall = (-380, 380)
        self.vertical_wall = (-280, 280)
        self.pace = 20
        self.speed(1)
        self.pause = False
        self.paddles = Paddle()
        self.UP_ANGLE = 90
        self.lower_buffer = 30
        self.higher_buffer = 60
        self.straight_line = 180
        self.DOWN_ANGLE = 270
        self.display = Screen()
        self.determine_direction()
        self.score = ScoreBoard()
        self.username = (self.display.textinput("Input Name", "What is your name?")).title()
        self.sleep_time = 0.07

    def move_ball(self):
        """This method controls the movement of the ball."""
        self.penup()
        self.control_paddles()
        self.rebound_wall()
        if self.pause:
            self.forward(STOP)
        else:
            self.forward(self.pace / 2)

    def game_over(self):
        """This method triggers the game over sequence"""
        if self.score.player_score > 2:
            self.score.clear()
            self.score.final_score(user=self.username, score=self.score.player_score)
            return True
        elif self.score.computer_score > 2:
            self.score.clear()
            self.score.final_score(user="Computer", score=self.score.computer_score)
            return True

    def control_paddles(self):
        """Handles User and AI paddle input actions"""
        self.display.listen()
        if self.xcor() < 0:
            self.display.onkey(fun=self.paddle_up, key="Up")
            self.display.onkey(fun=self.paddle_down, key="Down")
            self.display.onkey(fun=self.toggle_pause, key="space")
            self.paddle_hit(self.paddles.paddle_a)
        else:
            self.paddle_chasing()
            self.paddle_hit(self.paddles.paddle_b)

    def move_paddle(self, rackets, angle):
        """Controls User and AI paddle actions"""
        for racket in rackets:
            racket.setheading(angle)
            racket.forward(PADDLE_DISTANCE)
            # if rackets[0].ycor() < self.vertical_wall[1] and rackets[2].ycor() > self.vertical_wall[0]:
            #    racket.forward(7)
            # else:
            #    racket.back(7)

    def detect_paddle(self):
        """This method tells the program what paddle to  control."""
        if self.xcor() < 0:
            paddle = self.paddles.paddle_a
        else:
            paddle = self.paddles.paddle_b
        return paddle

    def paddle_up(self):
        """This method handles up movement of the paddle"""
        paddles = self.detect_paddle()
        self.move_paddle(paddles, self.UP_ANGLE)

    def paddle_down(self):
        """This method handles down movement of the paddle"""
        paddles = self.detect_paddle()
        self.move_paddle(paddles, self.DOWN_ANGLE)

    def rebound_wall(self):
        """This method handles the rebound action of the ball"""
        if self.distance(self.xcor(), self.vertical_wall[1]) < self.pace - self.lower_buffer / 2:
            new_heading = 360 - self.heading()
            self.setheading(new_heading)
        elif self.ycor() < self.vertical_wall[0] + self.pace / 2:
            new_heading = 360 - self.heading()
            self.setheading(new_heading)

    def hit_wall(self):
        """This launches the trigger to end the game."""
        if self.distance(self.horizontal_wall[1] + self.pace - 7, self.ycor()) < self.pace:
            self.score.player_score += 1
            self.score.clear()
            self.score.user_score()
            self.score.ai_score()
            self.sleep_time = 0.07
            return True
        if self.distance(self.horizontal_wall[0] - self.pace, self.ycor()) < self.pace:
            self.score.computer_score += 1
            self.score.clear()
            self.score.ai_score()
            self.score.user_score()
            self.sleep_time = 0.07
            return True

    def toggle_pause(self):
        """Just because I want to chill"""
        if self.pause:
            self.pause = False
        else:
            self.pause = True
        return self.pause

    def paddle_chasing(self):
        """AI response"""
        computer_paddle = self.paddles.paddle_b
        if self.ycor() > computer_paddle[1].ycor():
            self.paddle_up()
        else:
            self.paddle_down()

    def paddle_hit(self, paddles):
        """This method controls the action the ball will take after a paddle hits it."""
        for paddle in paddles:
            if self.distance(paddle) < self.pace + 5:
                if paddles.index(paddle) == 0:
                    if paddle.xcor() < 0:
                        new_heading = random.randint(self.lower_buffer, self.higher_buffer)
                        self.setheading(new_heading)
                    else:
                        new_heading = random.randint(
                            self.straight_line - self.higher_buffer, self.straight_line - self.lower_buffer)
                        self.setheading(new_heading)
                elif paddles.index(paddle) == 1:
                    if paddle.xcor() < 0:
                        new_heading = random.choice([random.randint(0, 16), random.randint(344, 359)])
                        self.setheading(new_heading)
                    else:
                        new_heading = 180 - self.heading()
                        self.setheading(new_heading)
                elif paddles.index(paddle) == 2:
                    if paddle.xcor() < 0:
                        new_heading = random.randint(
                            self.DOWN_ANGLE + self.lower_buffer, self.DOWN_ANGLE + self.higher_buffer)
                        self.setheading(new_heading)
                    else:
                        new_heading = random.randint(
                            self.straight_line + self.lower_buffer, self.straight_line + self.higher_buffer)
                        self.setheading(new_heading)
                self.sleep_time -= 0.005
                break
        return True
