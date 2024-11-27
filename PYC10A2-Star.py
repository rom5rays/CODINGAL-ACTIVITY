import turtle

my_turtle = turtle.Turtle()

for i in range(3):
    my_turtle.fd(100)
    my_turtle.left(120)
my_turtle.left(90)
my_turtle.penup()
my_turtle.fd(65)
my_turtle.right(90)
my_turtle.pendown()
for i in range(3):
    my_turtle.fd(100)
    my_turtle.right(120)

turtle.done()