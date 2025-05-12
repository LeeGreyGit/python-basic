import pygame
import sys

# 初期化
pygame.init()

# 画面サイズ
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("動く四角ゲーム")

# 色
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 四角の初期位置
x, y = 300, 220
speed = 5

# ゲームループ
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # キー操作
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # 四角を描画
    pygame.draw.rect(screen, RED, (x, y, 50, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
