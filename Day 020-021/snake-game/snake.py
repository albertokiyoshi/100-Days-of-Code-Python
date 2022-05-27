from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def move(self):
        for segment in range(len(self.body) - 1, 0, -1):
            x_position = self.body[segment - 1].xcor()
            y_position = self.body[segment - 1].ycor()
            self.body[segment].goto(x_position, y_position)
        self.body[0].forward(MOVE_DISTANCE)

    def add_segment(self, position):
        body_segment = Turtle("square")
        body_segment.color("white")
        body_segment.penup()
        body_segment.setpos(position)
        self.body.append(body_segment)

    def extend(self):
        self.add_segment(self.body[-1].position())


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
