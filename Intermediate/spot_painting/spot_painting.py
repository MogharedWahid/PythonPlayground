from turtle import Turtle,Screen
import colorgram
import random

def get_image_colors():
    m_rgb_colors = []
    colors = colorgram.extract('image.jpg', 30)
    # print(colors)
    for color in colors:
        r = color.rgb.r
        b = color.rgb.b
        g = color.rgb.g
        rgb_color = (r, g, b)
        m_rgb_colors.append(rgb_color)
    return m_rgb_colors

rgb_colors = get_image_colors()

screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.colormode(255)

turtle = Turtle()
turtle.shape('turtle')
turtle.speed('fastest')
turtle.penup()

def spot_paint(square_size):
    start_x = -(square_size * 50) / 2
    start_y = (square_size * 50) / 2
    turtle.goto(start_x, start_y)
    for i in range(square_size):
        for j in range(square_size):
            turtle.dot(20, random.choice(rgb_colors))
            turtle.fd(50)
        turtle.goto(start_x, start_y - (i + 1) * 50)


spot_paint(10)

screen.exitonclick()
