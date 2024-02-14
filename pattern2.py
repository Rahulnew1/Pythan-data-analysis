from turtle import*
speed(0)

def polygon(side):
    for _ in range(side):
        fd(100)
        lt(360/side)
# testing the function 

for i in range (6):
    polygon(10)
    polygon(5)
    lt(60)

hideturtle
mainloop()