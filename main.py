import time as t
from pygame import *
from random import randint
import os

init()
mixer.init()
font.init()

FPS=60
Game=True
PATH=__file__[:-8]

window = display.set_mode((700,500))
display.set_caption("PONG!")
display.set_icon(image.load("icon.png"))
bg = transform.scale(image.load(PATH+"\\BG\\5.png"), (700, 500))
clock = time.Clock()

mixer.music.load(PATH+"\\Sound\\music.wav")
t1 = t.time()
mixer.music.play()

Hit1 = mixer.Sound(PATH+"\\Sound\\Hit1.wav") # High pitch
Hit1_ = t.time()
Hit2 = mixer.Sound(PATH+"\\Sound\\Hit2.wav") # Low pitch
Hit2_ = t.time()

class GameSprite(sprite.Sprite):
    def __init__(self, speed, img, size_x, size_y, x, y, arg) -> None:
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(img), (size_x, size_y))
        self.speed = speed

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.other = arg

    def reset(self) -> None:
        window.blit(self.image, (self.rect.x, self.rect.y))

p1 = GameSprite(3, "plat.png", 5, 50, 3, 225, 0)
p2 = GameSprite(3, "plat.png", 5, 50, 690, 225, 0)
ball = GameSprite(4, PATH+"\\Skins\\2.png", 5, 5, 348, 248, [1, 1])

Fein = font.SysFont('Arial', 20)

while Game:
    Hit1__ = t.time()
    Hit2__ = t.time()
    t2 = t.time()
    if t2-t1 > 8:
        t1 = t.time()
        mixer.music.play()

    for e in event.get():
        if e.type == QUIT:
            Game = False

    window.blit(bg, (0, 0))
    p1.reset()
    p2.reset()
    ball.reset()

    keys = key.get_pressed()

    # ------- movement -------
    if keys[K_w] and p1.rect.y >= 55: p1.rect.y -= p1.speed
    if keys[K_s] and p1.rect.y <= 395: p1.rect.y += p1.speed
    if keys[K_p] and p2.rect.y >= 55: p2.rect.y -= p1.speed
    if keys[K_l] and p2.rect.y <= 395: p2.rect.y += p1.speed

    if keys[K_ESCAPE]: pass

    # ------- ball mov -------

    if ball.other[0]: ball.rect.x += ball.speed
    else: ball.rect.x -= ball.speed
    if ball.rect.x <= 5 and (ball.rect.y in range(p1.rect.y, p1.rect.y+50)):
        ball.other[0] = 1
        Hit1_ = t.time()
        Hit1.play()
    if ball.rect.x <= 5 and not (ball.rect.y in range(p1.rect.y, p1.rect.y+50)):
        ball.rect.x = 348
        ball.rect.y = 248

    if ball.rect.x >= 685 and (ball.rect.y in range(p2.rect.y, p2.rect.y+50)): 
        ball.other[0] = 0
        Hit1_ = t.time()
        Hit1.play()
    if ball.rect.x >= 685 and not (ball.rect.y in range(p2.rect.y, p2.rect.y+50)):
        ball.rect.x = 348
        ball.rect.y = 248
    if ball.other[1]: ball.rect.y += ball.speed
    else: ball.rect.y -= ball.speed
    if ball.rect.y <= 50:
        ball.other[1] = 1
        Hit2_ = t.time()
        Hit2.play()
    if ball.rect.y >= 445:
        ball.other[1] = 0
        Hit2_ = t.time()
        Hit2.play()
    

    display.update()
    clock.tick(FPS)