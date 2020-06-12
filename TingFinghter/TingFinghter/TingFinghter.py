import pygame

#initialization game
pygame.init()
#create a window
screen = pygame.display.set_mode((800,600))
#set tile
pygame.display.set_caption("Flighter Simulation")

#set icon
icon = pygame.image.load("C:\\Users\\am7574\\source\\repos\\TinyFinghter\\TingFinghter\\TingFinghter\\spaceship.png")
pygame.display.set_icon(icon)

#player
x_player = 370
y_player = 480
player_img = pygame.image.load("C:\\Users\\am7574\\source\\repos\\TinyFinghter\\TingFinghter\\TingFinghter\\space-invaders.png")

#define player

def player(x,y):
    screen.blit(player_img,(x,y))

running = True
while running:
    screen.fill((255,255,255))
    x_change = 0 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #check key stroke event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -10
                print(x_player)
            if event.key == pygame.K_RIGHT:
                x_change = 10
                print(x_player)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
    x_player += x_change

    #set boundary
    if x_player < 0:
        x_player = 0
    if x_player > 736:
        x_player = 736    
    player(x_player,y_player)
    pygame.display.update()