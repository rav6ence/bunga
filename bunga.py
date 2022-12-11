import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
t.pencolor('white')
t.speed(100)
col = ('aquamarine4', 'blue', 'blue4', 'blueviolet')

for n in range(5):
    for x in range(12):
        t.speed(x+10)
        for i in range(2):
            t.pensize(2)
            t.circle(80+n*20, 90)
            t.lt(90)
        t.lt(30)
    t.pencolor(col[n%4])
s.exitonclick()