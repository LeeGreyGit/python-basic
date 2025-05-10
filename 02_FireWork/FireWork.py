import pygame, sys, random, math
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
FPS = 60
SIZE = 4.5  # 爆発時の弾のサイズ
SPEED_CHANGE_SIZE = 0.05  # 爆発後の弾の縮小速度
CHANGE_SPEED = 0.07  # 弾の減速速度
RAD = math.pi/180  # ラジアンから度への変換
A_FALL = 1.5  # 重力加速度
NUM_BULLET = 50  # 1発の花火から出る弾の数
SPEED_MIN = 2  # 弾の最小速度
SPEED_MAX = 4  # 弾の最大速度
TIME_CREAT_FW = 40  # 発射間隔（フレーム数）
NUM_FIREWORKS_MAX = 3  # 同時発射される花火の最大数
NUM_FIREWORKS_MIN = 1  # 同時発射される花火の最小数
SPEED_FLY_UP_MAX = 12  # 打ち上がる弾の最大速度
SPEED_FLY_UP_MIN = 8  # 打ち上がる弾の最小速度

class Dot():  # 各弾の後を追う軌跡の点
	def __init__(self, x, y, size, color):
		self.x = x 
		self.y = y
		self.size = size
		self.color = color
	def update(self):
		# 点のサイズを縮小
		if self.size > 0:
			self.size -= SPEED_CHANGE_SIZE * 5
		else:
			self.size = 0
	def draw(self):  # 点を描画
		if self.size > 0:
			pygame.draw.circle(DISPLAYSURF, self.color, (int(self.x), int(self.y)), int(self.size))

class BulletFlyUp():  # 爆発前に上昇する弾
	def __init__(self, speed, x):
		self.speed = speed
		self.x = x
		self.y = WINDOWHEIGHT
		self.dots = []  # 軌跡の点のリスト
		self.size = SIZE / 2
		self.color = (255, 255, 100)

	def update(self):
		self.dots.append(Dot(self.x, self.y, self.size, self.color))  # 移動ごとに軌跡を追加
		# 弾の位置を更新
		self.y -= self.speed
		self.speed -= A_FALL * 0.1
		# 各点を更新
		for dot in self.dots:
			dot.update()
		# サイズが0以下の点を削除
		for dot in self.dots:
			if dot.size <= 0:
				self.dots.pop(self.dots.index(dot))

	def draw(self):
		pygame.draw.circle(DISPLAYSURF, self.color, (int(self.x), int(self.y)), int(self.size))  # 弾を描画
		# 各点を描画
		for dot in self.dots:
			dot.draw()

class Bullet():  # 爆発後に飛び散る弾
	def __init__(self, x, y, speed, angle, color):
		self.x = x
		self.y = y
		self.speed = speed
		self.angle = angle  # 弾の進行方向（角度）
		self.size = SIZE
		self.color = color

	def update(self):
		# 水平・垂直方向の速度を算出
		speedX = self.speed * math.cos(self.angle * RAD) 
		speedY = self.speed * -math.sin(self.angle * RAD)
		# 弾の位置を更新
		self.x += speedX
		self.y += speedY
		self.y += A_FALL
		# 弾のサイズを減少
		if self.size > 0:
			self.size -= SPEED_CHANGE_SIZE
		else:
			self.size = 0
		# 弾の速度を減少
		if self.speed > 0:
			self.speed -= CHANGE_SPEED
		else:
			self.speed = 0

	def draw(self):  # 弾を描画
		if self.size > 0:
			pygame.draw.circle(DISPLAYSURF, self.color, (int(self.x), int(self.y)), int(self.size))

class FireWork():  # 花火オブジェクト
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.dots = []  # 各弾の軌跡

		def creatBullets():  # 弾を生成する関数
			bullets = []
			color = Random.color()
			for i in range(NUM_BULLET):
				angle = (360 / NUM_BULLET) * i
				speed = random.uniform(SPEED_MIN, SPEED_MAX)
				bullets.append(Bullet(self.x, self.y, speed, angle, color))
			return bullets
		self.bullets = creatBullets()

	def update(self):
		for bullet in self.bullets:  # 各弾を更新
			bullet.update()
			self.dots.append(Dot(bullet.x, bullet.y, bullet.size, bullet.color))
		for dot in self.dots:  # 各点を更新
			dot.update()
		# サイズが0以下の点を削除
		for dot in self.dots:
			if dot.size <= 0:
				self.dots.pop(self.dots.index(dot))

	def draw(self):
		for bullet in self.bullets:  # 各弾を描画
			bullet.draw()
		for dot in self.dots:  # 各点を描画
			dot.draw()

class Random():
	def __init__(self):
		pass
		
	def color():  # ランダムな明るい色を生成
		color1 = random.randint(0, 255)
		color2 = random.randint(0, 255)
		if color1 + color2 >= 255:
			color3 = random.randint(0, 255)
		else:
			color3 = random.randint(255 - color1 - color2, 255)
		colorList = [color1, color2, color3]
		random.shuffle(colorList)
		return colorList

	def num_fireworks():  # 同時に打ち上げる花火の数
		return random.randint(NUM_FIREWORKS_MIN, NUM_FIREWORKS_MAX)

	def randomBulletFlyUp_speed():  # 弾の上昇速度をランダムに設定
		return random.uniform(SPEED_FLY_UP_MIN, SPEED_FLY_UP_MAX)

	def randomBulletFlyUp_x():  # 弾の水平位置をランダムに設定
		return random.randint(int(WINDOWWIDTH * 0.2), int(WINDOWHEIGHT * 0.8))

def main():
	global FPSCLOCK, DISPLAYSURF
	pygame.init()
	pygame.display.set_caption('FIREWORKS')
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	fireWorks = []
	time = TIME_CREAT_FW
	bulletFlyUps = []
	
	while True:
		DISPLAYSURF.fill((0, 0, 0))  # 背景をリセット
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()

		if time == TIME_CREAT_FW:  # 一定時間経過後に新しい弾を打ち上げる
			for i in range(Random.num_fireworks()):
				bulletFlyUps.append(BulletFlyUp(Random.randomBulletFlyUp_speed(), Random.randomBulletFlyUp_x()))

		for bulletFlyUp in bulletFlyUps: 
			bulletFlyUp.draw()
			bulletFlyUp.update()

		for fireWork in fireWorks:
			fireWork.draw()
			fireWork.update()

		for bulletFlyUp in bulletFlyUps:
			if bulletFlyUp.speed <= 0:  # 上昇が終了したら爆発させる
				fireWorks.append(FireWork(bulletFlyUp.x, bulletFlyUp.y))
				bulletFlyUps.pop(bulletFlyUps.index(bulletFlyUp))

		# 弾のサイズがなくなった花火を削除
		for fireWork in fireWorks:
			if fireWork.bullets[0].size <= 0:
				fireWorks.pop(fireWorks.index(fireWork))

		# 時間カウント更新
		if time <= TIME_CREAT_FW:
			time += 1
		else:
			time = 0

		pygame.display.update()
		FPSCLOCK.tick(FPS)

if __name__ == '__main__':
	main()
