from turtle import*

speed('fastest')
pencolor('yellow')
bgcolor('black')

for i in range (5):
    fd(100)
    for i in range (5):
        fd(75)
        lt(360/5)
        for i in range(5):
            fd(50)
            lt(360/5)
    
    lt(360/5)
    dot(10)

hideturtle()
mainloop()