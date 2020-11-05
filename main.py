# from colorgram import extract
#
# extracted_colors = extract('image.jpg', 30)
#
# colors = []
#
# for color in extracted_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colors.append((r, g, b))
#
# print(colors)

import turtle as t
from random import choice

color_list = [(224, 222, 217), (207, 153, 110), (221, 225, 223), (220, 204, 127), (140, 87, 68), (149, 160, 183), (202, 98, 75), (81, 86, 131), (120, 84, 96), (174, 155, 164), (179, 188, 213), (140, 153, 140), (56, 30, 38), (115, 37, 31), (153, 153, 90), (219, 179, 173), (48, 48, 108), (47, 35, 80), (216, 179, 187), (96, 105, 101), (93, 45, 53), (120, 136, 120), (113, 120, 155), (169, 107, 112), (94, 32, 29), (185, 196, 188), (186, 194, 196), (118, 133, 135)]

t.colormode(255)
tim = t.Turtle()
t.penup()
t.hideturtle()
t.speed("fastest")

for r in range(10):
    t.setx(0)
    t.sety(r * 30)
    for c in range(10):
        # setcolor
        color = choice((color_list))
        t.pencolor(color)

        # draw a dot
        t.pendown()
        t.begin_fill()
        t.dot(10)
        t.end_fill()
        t.penup()

        t.forward(30)


screen = t.Screen()
screen.exitonclick()