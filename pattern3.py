from turtle import*
speed(0)

def polygon(side,size,colour):
    fillcolor()
    begin_fill()
    for _ in range(side):
        fd(100)
        lt(360/side)
# testing the function 

for i in range (6):
    polygon(10,5,red)
    polygon(5)
    lt(60)

hideturtle
mainloop()