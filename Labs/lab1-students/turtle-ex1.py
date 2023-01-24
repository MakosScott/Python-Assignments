import turtle
s=turtle.Screen()
t=turtle.Turtle()

# Place your code after this line

#draw big  circle
t.penup()
t.goto(100,0)
t.pendown()
t.circle(100)

#draw 2nd circle
t.penup()
t.goto(100,20)
t.pendown()
t.circle(80)
#draw 3rd circle
t.penup()
t.goto(100,40)
t.pendown()
t.circle(60)

#draw 4rd circle
t.penup()
t.goto(100,80)
t.pendown()
t.circle(20)

#draw line 1
t.penup()
t.goto(-100,100)
t.pendown()
t.forward(400)
#draw line 2
t.penup()
t.goto(-100,300)
t.pendown()
t.setheading(315)
t.forward(550)
#draw line 3
t.penup()
t.goto(-100,-100)
t.pendown()
t.setheading(45)
t.forward(550)



