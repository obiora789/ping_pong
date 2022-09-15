from turtle import Screen
from setup import DrawDivider
from control import Control
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.bgcolor("black")
screen.tracer(0)
divider = DrawDivider()
divider.draw_divider()
controls = Control()

game_still_on = True
while game_still_on:
    time.sleep(controls.sleep_time)
    controls.move_ball()
    screen.update()
    if controls.hit_wall():
        controls.home()
        controls.determine_direction()
    if controls.game_over():
        game_still_on = False









screen.exitonclick()
