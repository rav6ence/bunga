import turtle 
t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
t.pencolor('magenta')
t.speed(100)

col = ('cyan', 'blue', 'blueviolet', 'magenta')

for n in range(5):
    for x in range(15):
        t.speed(x+20)
        for i in range(2):
            t.pensize(1)
            t.circle(80+n*20, 89)
            t.lt(90)
        t.lt(50)
    t.pencolor(col[n%4])
s.exitonclick()