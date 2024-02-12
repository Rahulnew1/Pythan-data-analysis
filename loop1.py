from turtle import*
speed('fastest')
pencolor('red')
pensize(5)

for i in range(8):
    fd(80)
    rt(45)
    write(f'n={i}',font=("calibri",16))


hideturtle()
mainloop()