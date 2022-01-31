import pygame
import random
pygame.init()
win=pygame.display.set_mode((900,600))

pygame.display.set_caption("GAME")

jump_an=pygame.image.load('jumpr.png')
go=pygame.image.load('gameover.png')
boom_an=[pygame.image.load('boom1.png'),pygame.image.load('boom2.png'),pygame.image.load('boom3.png'),
pygame.image.load('boom4.png'),pygame.image.load('boom5.png'),pygame.image.load('boom6.png'),pygame.image.load('boom7.png')]

left_an=[pygame.image.load('left1.png'),pygame.image.load('left2.png'),pygame.image.load('left3.png')]
right_an=[pygame.image.load('right1.png'),pygame.image.load('right2.png'),pygame.image.load('right3.png')]

bg = pygame.image.load('fon.jpg')
playerStand = pygame.image.load('stand.png')
bomb_pc=pygame.image.load('bomb_pc.png')
ht_pc1 = pygame.image.load('heart.png')
ht_pc2 = pygame.image.load('heart.png')
ht_pc3 = pygame.image.load('heart.png')
coin_pc= pygame.image.load('coin2.png')

clock=pygame.time.Clock()

xb=800
yb=425
speed_b=8
wight_b=50
left_b=51

xc=800
yc=425
score=0

x=200
y=380
wight= 70
length= 70
speed= 10
animcount_l=0
animcount_r=0
animcount_g=0
lives=3
jupm_count=12

left=False
right=False
jump=False
game_status=False
Gen = [random.randint(0,1) for i in range(20)]
i=0
flag=0
def Stolk():
	global x
	global y
	global xb
	global yb
	global lives
	global i
	global flag
	if x > xb-90 and x < xb+50 and y > yb-108:
		xb=800
		yb=425
		i+=1
		flag = Gen[i]
		lives-=1
		return True
	else:
		return False
def c_stolk():
	global x
	global y
	global xc
	global yc
	global score
	global i
	global flag
	if x > xc-90 and x < xc+50 and y > yc-108:
		xc=800
		yc=425
		i+=1
		flag = Gen[i]
		score+=1
		return True
	else:
		return False

def Boom_p():
    global game_status
    global animcount_g
    if game_status == True:
        win.blit(boom_an[animcount_g],(x,y))
        animcount_g+=1
    elif animcount_g != 0 and animcount_g < 7:
        win.blit(boom_an[animcount_g],(x,y))
        animcount_g+=1
    else:
        animcount_g = 0
    pygame.display.update()

def get_coin():
	global xc
	global yc
	global flag
	global i
	if xc > 0:
		xc-=speed_b
	else:
		i+=1
		flag = Gen[i]
		xc = 870
	win.blit(coin_pc,(xc,yc))
	pygame.display.update()

def drawBomb():
	global xb
	global yb
	global flag
	global i
	if xb > 0:
		xb-=speed_b
	else:
		i+=1
		flag = Gen[i]
		xb = 870
	win.blit(bomb_pc,(xb,yb))
	pygame.display.update()
def drawLives():
	global lives
	if lives == 3:
		win.blit(ht_pc1,(850,20))
		win.blit(ht_pc2,(790,20))
		win.blit(ht_pc3,(730,20))
	if lives == 2:
		win.blit(ht_pc1,(850,20))
		win.blit(ht_pc2,(790,20))
	if lives == 1:
		win.blit(ht_pc1,(850,20))
	pygame.display.update()
def drawPerson():
    global animcount_l
    global animcount_r
    global win
    clock.tick(30)
    if left:
        win.blit(left_an[animcount_l],(x,y))
        animcount_l+=1
        if animcount_l==3:
        	animcount_l=0
    elif right:
        win.blit(right_an[animcount_r],(x,y))
        animcount_r+=1
        if animcount_r==3:
        	animcount_r=0
    elif jump:
    	win.blit(jump_an,(x,y))
    else:
        win.blit(playerStand,(x,y))

    font = pygame.font.Font(None, 30)
    text = font.render("Score: "+ str(score),True,(255, 255,   0))
    win.blit(text, [730,80])
    pygame.display.update()

run=True

while run:
    clock.tick(30)
    win.blit(bg,(0, 0))
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run = False
    keys= pygame.key.get_pressed()
    if lives != 0:
        if keys[pygame.K_UP]:
            right = False
            left = False
            jump = True
        if jump:
    	    if jupm_count>=-12:
    		    if jupm_count <0:
    			    y+=(jupm_count**2)/2
    		    else:
    			    y-=(jupm_count**2)/2
    		    jupm_count-=1
    	    else:
    		    jump=False
    		    jupm_count=12
        else:
            if keys[pygame.K_LEFT] and x>5:
                x-=speed
                left=True
                right=False
                jump=False
            elif keys[pygame.K_RIGHT]and x<900-wight-5:
                x+=speed
                right=True
                left=False
                jump=False
            else:
    	        right=False
    	        left=False
        drawPerson()
        drawLives()
        Boom_p()
        game_status=Stolk()
        coin_st = c_stolk()
        if i == 19:
        	i = 0
        if flag:
        	drawBomb()
        else:
        	get_coin()
    else:
        win.blit(go,(120,120))
        pygame.display.update()
pygame.quit()
