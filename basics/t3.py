from turtle import *

start = 200
goto(-200,200)
while start >0:
    forward(start)
    left(360/6)
    start -= 10
    write(start, font=('arial',8,'normal'))

mainloop()
# 
from turtle import*

angle = 360/6
size = 100

forward(size)
left(angle)
forward(size)
left(angle)
forward(size)
left(angle)
forward(size)
left(angle)
forward(size)
left(angle)
forward(size)
left(angle)

mainloop()