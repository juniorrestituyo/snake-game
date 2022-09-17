import turtle as t
import random

SHAPES = ["circle", "triangle", "square"]
COLORS = ["blue", "red", "green", "yellow", "orange", "purple"]


class Food(t.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.shape(random.choice(SHAPES))
        self.color(random.choice(COLORS))
        self.goto(random_x, random_y)
