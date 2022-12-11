import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
for i in range(180):
    t.speed(0)
    t.color('blueviolet')
    t.circle(190 - i, 90)
    t.left(90)
    t.color('blue')
    t.circle(190 - i, 90)
    t.left(18)
s.exitonclick()