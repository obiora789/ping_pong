from turtle import Turtle
CURRENT_SCORE_FONT = ("Sans Serif", 38, "bold")
ALIGNMENT = "center"
FINAL_SCORE_FONT = ('Courier', 24, 'bold')
USER_DISPLAY = (-70, 240)
PC_DISPLAY = (70, 240)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.fillcolor("white")
        self.shape("square")
        self.shapesize(6, 6.5)
        self.player_score = 0
        self.computer_score = 0
        self.hideturtle()
        self.user_score()
        self.ai_score()

    def user_score(self):
        """Displays the User score"""
        self.goto(USER_DISPLAY)
        self.current_score(self.player_score)

    def ai_score(self):
        """Displays AI score"""
        self.goto(PC_DISPLAY)
        self.current_score(self.computer_score)

    def current_score(self, score):
        """Displays current score for both User and AI"""
        self.color("white")
        self.write(f"{int(score)}", move=False, align=ALIGNMENT, font=CURRENT_SCORE_FONT)

    def final_score(self, user, score):
        """This method displays the final score on the screen."""
        self.clear()
        self.goto(0, 0)
        self.color("white")
        self.write(f"Game Over! {user} Wins! The final score is "
                   f"{int(score)}.", move=False, align=ALIGNMENT,
                   font=FINAL_SCORE_FONT)
