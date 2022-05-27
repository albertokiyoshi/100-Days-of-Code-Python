from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.move_x = STARTING_MOVE_DISTANCE

    def create_car(self):
        if randint(1, 5) > 4:
            new_car = Car()
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.move_x)
            if car.xcor() < -320:
                self.cars.remove(car)

    def level_up(self):
        self.move_x += MOVE_INCREMENT


class Car(Turtle):

    def __init__(self):
        super().__init__()
        starting_y = randint(-250, 250)
        car_color = choice(COLORS)
        self.shape("square")
        self.color(car_color)
        self.shapesize(1, 2)
        self.penup()
        self.goto(320, starting_y)
