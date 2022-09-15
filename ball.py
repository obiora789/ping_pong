from turtle import Turtle
import random


class Ball(Turtle):
    """Ball class"""
    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.count = 0
        self.direction = [random.randint(0, 45), random.randint(315, 359)]
        self.west_begin = 135
        self.west_end = 225

    def determine_direction(self):
        """This determines the direction of the ball after each round"""
        self.count += 1
        if self.count % 2 == 0:
            direction = random.randint(self.west_begin, self.west_end)
            self.setheading(direction)
        else:
            direction = random.choice(self.direction)
            self.setheading(direction)
