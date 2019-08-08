import turtle
colors = ['orange','white','green']
turtle.bgcolor("Black")
t = turtle.Pen()


t.speed(100)
for x in range(360):
    t.pencolor(colors[x%3])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)
    #s.circle(5*i)
    #s.circle(-5*i)
    #s.left(i)
turtle.exitonclick()