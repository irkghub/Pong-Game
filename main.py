

from turtle import Screen, Turtle
from player import Player
from pong import Pong
import time
from score import Scoreboard

screen = Screen()
screen.bgcolor("maroon")
screen.setup(800,600)
screen.title("Pong Game")
screen.tracer(0)
score = Scoreboard()
pong = Pong()

player_right = Player(350,0)
player_left = Player(-350,0)

screen.listen()

screen.onkey(player_right.move_up,"k")
screen.onkey(player_right.move_down,"l")
screen.onkey(player_left.move_up,"s")
screen.onkey(player_left.move_down,"d")

ceiling = 280
floor = -280

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    pong.move()
    if pong.ycor() > ceiling or pong.ycor() < floor:
        pong.bounce_top_bottom()

#   Detect collision with the  player
    if pong.distance(player_right) < 50 and pong.xcor() == 330 or pong.distance(player_left) < 50 and pong.xcor() == -330:
        pong.bounce_back()

    if pong.xcor() == 390:
        score.left_scorecard()
        pong.base_position()
        pong.bounce_back()

    if pong.xcor() == -390:
        score.right_scorecard()
        pong.base_position()
        pong.bounce_back()

