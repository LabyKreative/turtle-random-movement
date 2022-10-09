import turtle as t
import random

jim = t.Turtle()
jim.shape("turtle")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


#
#
# directions = [0, 90, 180, 270]
# jim.pensize(15)
# # jim.speed("fastest")
#
# for _ in range(200):
#     jim.color(random_color())
#     jim.fd(30)
#     jim.setheading(random.choice(directions))


jim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        jim.color(random_color())
        jim.circle(100)
        jim.setheading(jim.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
