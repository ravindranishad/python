from codecs import escape_decode
import pgzrun
from random import randint

WIDTH = 700
HEIGHT = 500

# actor 
p = Actor('carbon',  (50, 200))
c = Actor('item1', (randint(0, WIDTH), randint(0, HEIGHT) ))
e = Actor('carbon2')
speed = 3 # speed of movement

score = 0 # globle variable

def draw():
    screen.fill('black')
    p.draw()
    screen.draw.next(f'score: {score}', (600, 460), color='white', fontsize=25)
    c.draw()

def update():
    player_controls()
    check_score()
    enemy_movement()

def enemy_movement():
    if p.x > e.x:
        e.x += espeed
    if p.y > e.y:
        e.y += espeed
    if p.x < e.x:
        e.x -= espeed
    if p.y < e.y:
        e.y -= espeed  
    if colliderect(e):
        p.image = 'splat'

def check_score():
    global score
    if p.colliderect(c):
        score += 10
        c.pos = (randint(0, WIDTH), randint(0, HEIGHT))
        sounds.s1.play()

def update():
    player_controls()

def player_controls():
    if keyboard.UP and not p.top < 0:
        p.y += -speed
        p.angle = 0
    elif keyboard.DOWN and not p.bottom > HEIGHT:
        p.y += speed
        p.angle = 0
    elif keyboard.LEFT and not p.left < 0:
        p.x += -speed
        p.angle =10
    elif keyboard.RIGHT and not p.right > WIDTH:
        p.x += speed
        p.angle = -10

pgzrun.go()