from turtle import Turtle


class Winner(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto((0, 200))
        self.hideturtle()
        self.color("black")
        self.write(f"You have guessed them all, congrats!", font=("Arial", 29, "bold"), align="center")
