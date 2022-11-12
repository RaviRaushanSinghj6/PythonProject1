from turtle import *
penup()
s = getscreen()
s.bgcolor("black")
pencolor("white")
goto(200,200)
pendown()
fillcolor("lightblue")
begin_fill()
goto(-200, 200)
goto(-200,-200)
goto(200,-200)
goto(200,200)
end_fill()

# Drawing squares
txy = [(150,150,"navy"),(-25,150,"olive"), (-25,-25,"maroon"),(150,-25,"red")]
for xyc in txy:
    x,y,c= xyc
    penup()
    goto(x,y)
    pendown()
    fillcolor(c)
    begin_fill()
    goto(x-125,y)
    goto(x-125,y-125)
    goto(x,y-125)
    goto(x,y)
    end_fill()
ht
