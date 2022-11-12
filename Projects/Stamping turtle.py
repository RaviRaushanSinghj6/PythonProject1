from turtle import *

s = getscreen()

shape("square")
pencolor("red")
fillcolor("yellow")
pensize(1)
shapesize(2, 2, 2)

penup()
goto(200,200)
stamp()
goto(-200,200)
stamp()
goto(-200,-200)
stamp()
goto(200,-200)
stamp()

