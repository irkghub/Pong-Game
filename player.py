from turtle import Turtle 


class Player(Turtle):
    
    def __init__(self, x, y):
        super().__init__()

        self.penup()
        self.color("lavender")
        self.shape("square")
        self.shapesize(5, 1, 1)
        self.setposition(x, y)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        