import pgzrun

WIDTH= 800
HEIGHT= 500

def draw():
    screen.draw.text(
        "hello , pygame zero!",
        center=(WIDTH/2,HEIGHT/2),
        fontsize=32,
        colour="yellow"
    )
def update():
    pass

pgzrun.go()