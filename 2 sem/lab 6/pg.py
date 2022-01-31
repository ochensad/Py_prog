import pygame as pg


BLUE=(145,159,245)
RED =(245,105,180)
WHITE=(255,255,255)

pg.init()
win=pg.display.set_mode((600,400))
clock=pg.time.Clock()

rot = 0
rot_speed = 3
sqrt = pg.Surface((100 , 100))
sqrt.set_colorkey(WHITE)
sqrt.fill(BLUE)

x = 100
y = 100
rect = sqrt.get_rect()
rect.center= (x,y)

run=True
speed = 5
while run:
	win.fill(WHITE)
	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
	if x < 550 and y == 100:
		x+=speed
	else:
		if y < 330 and x >= 550:
			y+=speed
		else:
			if x > 50:
				x-=speed
			else:
				if y > 100:
					y-=speed
				else:
					x=100
					y=100

	last=(x,y)
	rot=(rot+rot_speed) %360
	new = pg.transform.rotate(sqrt, rot)
	rect = new.get_rect()
	rect.center = last
	win.blit(new, rect)

	pg.display.update()
	clock.tick(60)
pg.quit()