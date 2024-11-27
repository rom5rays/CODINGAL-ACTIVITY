import turtle

my_turtle = turtle.Turtle()
no_sides = int(input('number of sides of polygon:'))
angle = 360//no_sides


my_turtle.color('red')
my_turtle.begin_fill()
for i in range(no_sides):
    my_turtle.forward(90)
    my_turtle.left(angle)
my_turtle.end_fill()
my_turtle.hideturtle()

turtle.done()