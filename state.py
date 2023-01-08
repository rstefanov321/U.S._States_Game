from turtle import Turtle


class State(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto((float(x), float(y)))
        self.write(f"{state}", font=("Arial", 12, "bold"), align="center")
