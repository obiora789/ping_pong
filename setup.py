from turtle import Turtle
POSITIONS_A = [(-370, 20), (-370, 0), (-370, -20)]
POSITIONS_B = [(360, 20), (360, 0), (360, -20)]


class Paddle:
    """This is the class that handles paddle creation."""
    def __init__(self):
        self.paddle_a = self.create_paddle(POSITIONS_A)
        self.paddle_b = self.create_paddle(POSITIONS_B)

    def create_paddle(self, positions):
        """This method creates both paddles; one at a time."""
        paddle_list = []
        for position in positions:
            part_paddle = Turtle("square")
            part_paddle.color("white")
            part_paddle.penup()
            part_paddle.goto(position)
            paddle_list.append(part_paddle)
        return paddle_list


class DrawDivider(Turtle):
    """This class draws the dividing line at the middle of the screen."""
    def __init__(self):
        super().__init__()
        self.pace = 20
        self.start_draw = (0, -290)
        self.end_draw = 300
        self.UP_ANGLE = 90

    def draw_divider(self):
        self.penup()
        self.goto(self.start_draw)
        self.setheading(self.UP_ANGLE)
        self.pencolor("white")
        self.hideturtle()
        while self.ycor() < self.end_draw:
            self.pendown()
            self.forward(self.pace)
            self.penup()
            self.forward(self.pace)






