from turtle import *
import time

s = getscreen()
s.bgcolor("brown")
title("Moving turtle")
pencolor("blue")
shape("turtle")
# forward(12)
shapesize(10, 10, 5)
for angle in range(0, 1000, 1):

    left(angle)
    # time.sleep(2)
