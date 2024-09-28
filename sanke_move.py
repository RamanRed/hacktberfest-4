from turtle import Screen, Turtle
from random import randint

class SnakeMove:
    HighScore = 0
    src = Screen()
    snake_obj = []
    head = None

    def __init__(self):
        # Initialize the snake with three segments
        for i in range(3):
            segment = Turtle(shape="square")
            segment.resizemode("user")
            segment.shapesize(5 / 4, 5 / 4)
            segment.goto((-i) * 10, 0)
            segment.color("gray")
            segment.penup()
            self.snake_obj.append(segment)
        self.head = self.snake_obj[0]

    def reset(self):
        # Reset the game state
        for segment in self.snake_obj:
            segment.goto(1000, 1000)  # Consider how this impacts game state
        self.snake_obj = []
        self.__init__()

    def grow(self):
        # Add a new segment to the snake
        x1, y1 = self.head.xcor(), self.head.ycor()  # Initialize x1, y1 for position tracking
        for index in range(len(self.snake_obj)):
            if index != 0:
                # Track the previous segment's position
                prev_x = self.snake_obj[index].xcor()
                prev_y = self.snake_obj[index].ycor()
                self.snake_obj[index].goto(x1, y1)
                x1, y1 = prev_x, prev_y
            else:
                self.snake_obj[index].forward(20)

        new_segment = Turtle(shape="square")
        new_segment.resizemode("user")
        new_segment.shapesize(5 / 4, 5 / 4)
        new_segment.color("gray")
        new_segment.penup()
        self.snake_obj.append(new_segment)

    def move(self):
        # Move the snake based on its segments
        self.grow()  # You may want to rethink how movement and growth are handled
        self.src.update()

    def set_direction(self, direction):
        # Set the snake's heading based on user input
        if direction == "up" and self.head.heading() != 270:
            self.head.setheading(90)
        elif direction == "down" and self.head.heading() != 90:
            self.head.setheading(270)
        elif direction == "left" and self.head.heading() != 0:
            self.head.setheading(180)
        elif direction == "right" and self.head.heading() != 180:
            self.head.setheading(0)

class Food(Turtle):
    def __init__(self):
        super().__init__()

    def random_position(self, snake_segments):
        occupied_positions = [(seg.xcor(), seg.ycor()) for seg in snake_segments]
        while True:
            x = randint(-340, 340)
            y = randint(-340, 340)
            if (x, y) not in occupied_positions:
                break

        self.shape("circle")
        self.shapesize(5 / 4, 5 / 4)
        self.color("red")
        self.penup()
        self.goto(x, y)

    def check_eat(self, snake_head):
        return self.distance(snake_head) <= 20

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def display_score(self, score):
        self.clear()
        self.penup()
        self.write(f"Score: {score}", align="center", font=("Arial", 20, "normal"))

    def display_high_score(self, high_score):
        self.clear()
        self.penup()
        self.goto(-100, 360)
        self.write(f"High Score: {high_score}", align="center", font=("Arial", 20, "normal"))

def game_over():
    over_message = Turtle()
    over_message.hideturtle()
    over_message.color("#000000")
    over_message.write("Game OVER", align="center", font=("Arial", 24, "normal"))

def check_collision(snake_segments):
    for segment in snake_segments[3:]:
        if snake_segments[0].distance(segment) <= 20:
            game_over()
            return True
    return False
