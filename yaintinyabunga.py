import turtle
import colorsys

turtle.setup(600,600)
turtle.speed(0)
turtle.tracer(50)
turtle.width(2)
turtle.screensize(70)
turtle.bgcolor('purple')

for j in range (25):
    for i in range (15):
        turtle.color(colorsys.hsv_to_rgb(i/15,j/25,1))
        turtle.right(50)
        turtle.circle(100-j*4,90)
        turtle.left(90)
        turtle.circle(100-j*4,90)
        turtle.right(50)
        turtle.circle(5,24)
turtle.hideturtle()
turtle.done