import pygame
pygame.init()
display_width = 600
display_height = 480
surface = pygame.display.set_mode((display_width, display_height))
background = pygame.image.load('beach.png')
boat = pygame.image.load('boat.png')
boat_width=boat.get_size()[0]
boat_height = boat.get_size()[1]
boatx = 30
boaty = display_height - boat_height+10
brown = (86, 58, 11)
blue = (105, 193, 242)
tan = (242, 226, 105)
boat_speedx = 0
boat_speedy = 0
def quit_game():
    pygame.quit()
    quit()

while True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit_game()
        if event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_UP and boaty>10:
                boat_speedy=-5
        
            if event.key ==pygame.K_DOWN and boaty<display_height-10-boat_height:
                boat_speedy=5
            if event.key == pygame.K_RIGHT and boatx<display_width-10:
                boat_speedx= 5
            if event.key == pygame.K_LEFT and boatx>10:
                boat_speedx = -5
        if event.type ==pygame.KEYUP:
            if event.key ==pygame.K_UP and boaty>10:
                boat_speedy=0
        
            if event.key ==pygame.K_DOWN and boaty<display_height-10-boat_height:
                boat_speedy=0
            if event.key == pygame.K_RIGHT and boatx<display_width-10:
                boat_speedx= 0
            if event.key == pygame.K_LEFT and boatx>10:
                boat_speedx = 0
    boatx += boat_speedx
    boaty += boat_speedy
        
    surface.blit(background, (0,0))
    surface.blit(boat, (boatx-8, boaty-8))
    if (surface.get_at((boatx, boaty))== tan or surface.get_at((boatx+boat_width, boaty))==tan or
        surface.get_at((boatx,boaty+boat_height-30))==tan or surface.get_at((boatx+boat_width,boaty+boat_height-30))==tan):
            print('win')        
    if (surface.get_at((boatx, boaty))== brown or surface.get_at((boatx+boat_width, boaty))==brown or
        surface.get_at((boatx,boaty+boat_height-15))==brown or surface.get_at((boatx+boat_width,boaty+boat_height-15))==brown):
            quit_game()
    if surface.get_at((boatx, boaty))==tan:
        print('You win')
    pygame.display.update()
    