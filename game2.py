import pgzrun
import random

HIGHT=500
WIDTH=800

class Hero(Actor):
    def move(self):
        if keyboard.left:
            self.x-=5
        elif keyboard.right:
            self.x+=5
        elif keyboard.up:
            self.y-=5
        elif keyboard.down:
            self.y+=5
        else:
            self.angle=0

    def warp(self):
        if self.x> WIDTH:
            self.x =0
        if self.x<0:
            self.x=WIDTH
        if self.y> HIGHT:
            self.Y =0
        if self.Y<0:
            self.Y=HIGHT
        

class duck(Actor):
    def track(self,player,speed=1):
        if player.x > self.x:
            self.x += speed
        elif player.x < self.x:
            self.x -= speed
        if player.y> self.y:
            self.y += speed
        elif player.y <self.y:
            self.y-= speed



p=Hero('mario',(100,100))
b=Rect((300,100),(50,50))
s=duck('duck',(1000.1000))
e=sneak('sneak',(300,1000))

def draw():
    screen.fill('white')
    p.draw()
    s.draw()
    e.deaw()
    screen.draw.filled_rect(b,'blue')

def update():
    p.move()
    p.move()
    s.track(P,4)
    e.track(p,1)

pgzrun.go()

