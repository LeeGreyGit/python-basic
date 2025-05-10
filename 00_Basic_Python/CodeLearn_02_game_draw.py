import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Draw')

# あらかじめ色を定義
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(WHITE)

    pygame.draw.rect(DISPLAYSURF, RED, (10, 10, 100, 50))  # 四角形（塗りつぶし）
    pygame.draw.rect(DISPLAYSURF, GREEN, (150, 10, 100, 50), 2)  # 四角形（枠線のみ）
    '''
    pygame.draw.circle(surface, color, center, radius, width) は円を描画する関数です。
        surface は描画先のサーフェス。
        color は描画する色。
        center は円の中心座標を表すタプル（またはリスト）。
        radius は半径。
        width は線の太さ（四角形と同様）。
    '''
    pygame.draw.circle(DISPLAYSURF, RED, (50, 100), 20)  # 円（塗りつぶし）
    pygame.draw.circle(DISPLAYSURF, BLUE, (200, 100), 20, 1)  # 円（枠線のみ）
    '''
    pygame.draw.ellipse(surface, color, rect, width) は楕円を描画する関数です。
        surface は描画先のサーフェス。
        color は描画する色。
        rect は四角形の情報を含む4要素のタプル（またはリスト）で、楕円はこの矩形内に内接します。
        width は線の太さ（四角形と同様）。
    '''
    pygame.draw.ellipse(DISPLAYSURF, RED, (10, 150, 100, 50))  # 楕円（塗りつぶし）
    pygame.draw.ellipse(DISPLAYSURF, GREEN, (150, 150, 100, 50), 3)  # 楕円（枠線のみ）
    '''
    pygame.draw.polygon(surface, color, points, width) は多角形を描画する関数です。
        surface は描画先のサーフェス。
        color は描画する色。
        points は頂点の座標を表すタプル（またはリスト）の集合。各頂点はタプル（またはリスト）で指定します。
        width は線の太さ（四角形と同様）。
    '''
    pygame.draw.polygon(DISPLAYSURF, RED, ((10, 220), (150, 230), (100 ,290), (30, 270)))  # 多角形（塗りつぶし）
    pygame.draw.polygon(DISPLAYSURF, BLUE, ((160, 220), (300, 230), (250 ,290), (180, 270)), 2)  # 多角形（枠線のみ）
    '''
    pygame.draw.line(surface, color, start_pos, end_pos, width) は直線を描画する関数です。
        surface は描画先のサーフェス。
        color は描画する色。
        start_pos は始点の座標を表すタプル（またはリスト）。
        end_pos は終点の座標を表すタプル（またはリスト）。
        width は線の太さ。
    '''
    pygame.draw.line(DISPLAYSURF, BLACK, (300, 50), (350, 150), 4)  # 直線

    pygame.display.update()
