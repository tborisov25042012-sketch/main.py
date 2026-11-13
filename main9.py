import random
import turtle
print( "Твое число:",random.randint(1, 100))
t = turtle.Turtle()
t.shape("turtle")
t.color("red")
turtle.speed(10)
for i in range(36):
    t.right(10)
    t.circle(100)