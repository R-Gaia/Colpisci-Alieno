from pgzero.clock import clock
from random import randint
import pgzrun
TITLE = "Colpisci l'alieno"
WIDTH = 1000
HEIGHT = 1000
messaggio = ""
alieno = Actor("alieno")
def draw():
    screen.clear()
    screen.fill(color=(0,0,100))
    alieno.draw()
    screen.draw.text(messaggio, center=(400, 40), fontsize=60)
def piazza_alieno():
    '''
    Il limite di 50 pixel è definito per evitare che l'immagine
    sia parzialmente fuori schermo
    Alieno ha size 64x64
    '''
    alieno.x = randint(50, WIDTH-50)
    alieno.y = randint(50, HEIGHT-50)
    alieno.image = "alieno"
def on_mouse_down(pos):
    global messaggio
    if alieno.collidepoint(pos):
        messaggio = "Bel colpo!"
        alieno.image = "esplosione"
    else:
        messaggio = "Mancato..."
piazza_alieno()
clock.schedule_interval(piazza_alieno, 1.0)
pgzrun.go() 