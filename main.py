#from winreg import REG_REFRESH_HIVE#
import pygame
import random
pygame.init()

win = pygame.display.set_mode((500 , 500))
pygame.display.set_caption("First Game")


x = 50
y = 50
width = 40
height = 60
vel = 5 

run = True 

while run:
    
    pygame.time.delay(100)

    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            run = False

    keys  = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel 
		
    if keys[pygame.K_RIGHT]:
        x += vel
		
    if keys[pygame.K_UP]:
        y -= vel
		
    if keys[pygame.K_DOWN]:
        y += vel

    RED_VALUE = random.randint(0, 255)
    GREEN_VALUE = random.randint(0, 255)
    BLUE_VALUE = random.randint(0, 255)

	#win.fill((0,0,0))#
    pygame.draw.rect(win, (RED_VALUE, GREEN_VALUE, BLUE_VALUE), (x, y, width, height))
    pygame.display.update()

pygame.quit()