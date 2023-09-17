from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.penup()
        self.for_left()
        self.for_center()
        self.for_right()

    def for_left(self):
        self.setposition(-150, 265)
        self.write(f"{self.score_left}", False, "left", ("Arial", 24, "normal"))

    def for_center(self):

        self.setposition(0,265)
        self.hideturtle()
        self.write("Score", False, "center", ("Arial", 24, "normal"))

    def for_right(self):

        self.setposition(150, 265)
        self.write(f"{self.score_right}", False, "right", ("Arial", 24, "normal"))

    def left_scorecard(self):
        self.score_left += 1
        self.clear()
        self.setposition(-150, 265)
        self.write(f"{self.score_left}", False, "left",("Arial", 24, "normal"))
        self.for_center()
        self.for_right()

    def right_scorecard(self):
        self.score_right += 1
        self.clear()
        self.setposition(150, 265)
        self.write(f"{self.score_right}", False, "right", ("Arial", 24, "normal"))
        self.for_left()
        self.for_center()


