import pgzrun
import random

class Hero(Actor):
    def move(self):
        if keybord.left:
            self.x-=5
        elif keybord

HIGHT=500
WIDTH=800
p=Hero('mario',(100,100))
b=Rect((300,100),50,50)
def draw():
    screen.fill('white')
    p.draw()
    screen.drow.filled_rect(b,'blue')
def update():
    pass

pgzrun.go()

