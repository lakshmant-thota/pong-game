from turtle import Turtle

# TODO 2 : Create and move a paddle
# TODO 3 : Create another Paddle
PADDLE_Y_INC = 20
class Paddle(Turtle):

    def __init__(self, x, y, left_or_right):
        super().__init__()
        self.shape("square")
        if left_or_right == "left":
            self.color("midnight blue")
        else:
            self.color("dark green")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)

    def go_up(self):
        new_y = self.ycor() + PADDLE_Y_INC
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - PADDLE_Y_INC
        self.goto(self.xcor(), new_y)
