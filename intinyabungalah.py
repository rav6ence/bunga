import turtle
import colorsys

turtle.setup(600,600)
turtle.speed(0)
turtle.tracer(180)
turtle.width(2)
turtle.screensize(70)
turtle.bgcolor('black')

for j in range (25):
    for i in range (15):
        turtle.color(colorsys.hsv_to_rgb(i/15,j/25,1))
        turtle.right(90)
        turtle.circle(200-j*4,90)
        turtle.left(90)
        turtle.circle(200-j*4,90)
        turtle.right(1800)
        turtle.circle(5,24)
turtle.hideturtle()
turtle.done