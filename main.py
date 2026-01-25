from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < height - 100:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - 100:
            self.rect.y += self.speed

back = (200, 255, 255)
width = 600
height = 500
win = display.set_mode((width,height))
win.fill(back)

racket1 = Player('racket.png',30, 200, 20, 100, 10)
racket2 = Player('racket.png',550, 200, 20, 100, 10)
ball = GameSprite('tenis_ball.png', 250, 250, 50, 50, 5)

FPS = 60
game = True
finish = False
clock = time.Clock()

speed_x = 3
speed_y = 3

font.init()
font = font.Font(None, 40)
win_1 = font.render("Первый игрок победил!", True, (0, 255, 0))
win_2 = font.render("Второй игрок победил!", True, (0, 255, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        win.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > height - 50 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1

    if ball.rect.x < 0:
        win.blit(win_2, (100, 100))
        finish = True
        game = False
        
    if ball.rect.x > width - 50:
        win.blit(win_2, (100, 100))
        finish = True
        game = False
    
    racket1.reset()
    racket2.reset()
    ball.reset()
    
    display.update()
    clock.tick(FPS)
