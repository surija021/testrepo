import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

dist = 5
tess.up()                       # not to leave a mark behind
for _ in range(30):   			# start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(dist)          # move tess along
    tess.right(24)              # and turn her
    dist = dist + 2
wn.exitonclick()				# remove screen when click

#tess.penup()					#??


#IMPORT MODULE
import random
prob = random.random()
result = prob * 5
print(prob)
print(result)

#IMPORT MODULE (2)
#import random
from random import random
#prob = random.random()
prob=random()
result = prob * 5
print(prob)
print(result)

