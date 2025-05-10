import pygame, sys
from pygame.locals import *
import os

WINDOWWIDTH = 400  # ウィンドウの幅
WINDOWHEIGHT = 450  # ウィンドウの高さ

WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)

pygame.init()
base_path = os.path.dirname(__file__)
img_path = os.path.join(base_path, 'img', 'car.png')

### FPSの設定 ###
FPS = 60  # FPS（フレーム毎秒）1秒間に描画するフレーム数
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Animation')

# フォントを設定してテキストをサーフェスに描画
font = pygame.font.SysFont('consolas', 30)
textSurface = font.render('Hello world!', True, GREEN, RED)

### サーフェスを作成し、車の形を描く ###
# car_x = 0  # 車のX座標
# carSurface = pygame.Surface((100, 50), SRCALPHA)
# pygame.draw.polygon(carSurface, RED, ((15, 0), (65, 0), (85, 15), (100, 15), (100, 40), (0, 40), (0, 15)))
# pygame.draw.circle(carSurface, GREEN, (15, 40), 10)
# pygame.draw.circle(carSurface, GREEN, (85, 40), 10)

class Car_draw():
    def __init__(self):
        self.x = 0  # 車のX座標
        # サーフェスを作成し、車の形を描く
        self.surface = pygame.Surface((100, 50), SRCALPHA)  # SRCALPHA: 透明なサーフェス（指定しないと黒背景になる）
        pygame.draw.polygon(self.surface, RED, ((15, 0), (65, 0), (85, 15), (100, 15), (100, 40), (0, 40), (0, 15)))
        pygame.draw.circle(self.surface, GREEN, (15, 40), 10)
        pygame.draw.circle(self.surface, GREEN, (85, 40), 10)

    # 車を描画する
    def draw(self):
        DISPLAYSURF.blit(self.surface, (self.x, 100))

    # 車の位置を更新する
    def update(self):
        self.x += 2
        if self.x + 100 > WINDOWWIDTH:
            self.x = WINDOWWIDTH - 100

class Car_image():
    def __init__(self):
        self.x = 0  # 車のX座標
        # サーフェスを作成し、画像で車を描画
        self.surface = pygame.image.load(img_path)

    # 車を描画する
    def draw(self):
        DISPLAYSURF.blit(self.surface, (self.x, 200))

    # 車の位置を更新する
    def update(self):
        self.x += 2
        if self.x + 100 > WINDOWWIDTH:
            self.x = WINDOWWIDTH - 100

class Car_move():
    def __init__(self):
        self.x = 0  # 車のX座標
        # サーフェスを作成し、画像で車を描画
        self.surface = pygame.image.load(img_path)

    # 車を描画する
    def draw(self):
        DISPLAYSURF.blit(self.surface, (self.x, 300))

    # キー入力で車の位置を変更する
    def update(self, moveLeft, moveRight):
        if moveLeft == True:
            self.x -= 2
        if moveRight == True:
            self.x += 2

        if self.x + 100 > WINDOWWIDTH:
            self.x = WINDOWWIDTH - 100
        if self.x < 0:
            self.x = 0

car_draw = Car_draw()
car_image = Car_image()
car_move = Car_move()
moveLeft = False
moveRight = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moveLeft = True
            if event.key == K_RIGHT:
                moveRight = True

        if event.type == KEYUP:
            if event.key == K_LEFT:
                moveLeft = False
            if event.key == K_RIGHT:
                moveRight = False
    # ウィンドウの背景色を設定
    DISPLAYSURF.fill(WHITE)
    # テキストを表示
    DISPLAYSURF.blit(textSurface, (100, 20))
    # 車を描画（図形）
    car_draw.draw()
    car_draw.update()
    # 車を描画（画像）
    car_image.draw()
    car_image.update()
    # 車を描画（移動対応）
    car_move.draw()
    car_move.update(moveLeft, moveRight)
    # DISPLAYSURF.blit(carSurface, (car_x, 100))

    ### 車の位置を更新する ###
    # car_x += 2
    # if car_x + 100 > WINDOWWIDTH:
    #     car_x = WINDOWWIDTH - 100

    pygame.display.update()
    fpsClock.tick(FPS)
