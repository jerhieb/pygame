import pygame
pygame.init()
display_width = 100
display_height = 200
surface = pygame.display.set_mode((display_width, display_height))
ship = pygame.image.load('Birdship.png')
ship_background = pygame.image.load('ship background.png')
pygame.mixer.music.load('spacemusic.wav')
pygame.mixer.music.play(-1)
ship_x = 50
ship_y = 100
ship_xvel = 0
ship_yvel = 0
back_x = 0
back_y = 0
last_direction = 'up'
lives = 3
def win():
    surface.fill((0,0,0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship_xvel = 7
                back_x = back_x - 7
                last_direction = 'right'
            if event.key == pygame.K_LEFT:
                ship_xvel = -7
                back_x = back_x + 7
                last_direction = 'left'
            if event.key == pygame.K_UP:
                ship_yvel = -7
                back_y = back_y +7
                last_direction ='up'
            if event.key == pygame.K_DOWN:
                ship_yvel = 7
                bacK_y = back_y - 7
                last_direction ='down'
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship_xvel = 0
            if event.key == pygame.K_LEFT:
                ship_xvel = 0
            if event.key == pygame.K_UP:
                ship_yvel = 0
            if event.key == pygame.K_DOWN:
                ship_yvel = 0       
    ship_x = ship_x + ship_xvel
    ship_y = ship_y + ship_yvel
    
    if last_direction == 'up':
        r_ship = pygame.transform.rotate(ship, 0)
        
    if last_direction == 'right':
        r_ship = pygame.transform.rotate(ship, -90)
    if last_direction == 'left':
        r_ship = pygame.transform.rotate(ship, 90)
    if last_direction == 'down':
        r_ship = pygame.transform.rotate(ship, 180)
    
    if surface.get_at((ship_x, ship_y))==(238, 254, 26, 255):
        ship_x = 50
        ship_y = 100
        lives = lives - 1
    if surface.get_at((ship_x +r_ship.get_width(), ship_y))==(238, 254, 26, 255):
        ship_x = 50
        ship_y = 100
        lives -= 1
    if surface.get_at((ship_x, ship_y+r_ship.get_height()))==(238, 254, 26, 255):
        ship_x = 50
        ship_y = 100
        lives -= 1
    if surface.get_at((ship_x +r_ship.get_width(), ship_y+r_ship.get_height()))==(238, 254, 26, 255):
        ship_x = 50
        ship_y = 100
        lives -=1
    if surface.get_at((ship_x, ship_y))==(63, 87, 210, 255):
        print('you win')
    if surface.get_at((ship_x +r_ship.get_width(), ship_y))==(63, 87, 210, 255):
        print('you win')
    if surface.get_at((ship_x, ship_y+r_ship.get_height()))==(63, 87, 210, 255):
        print('you win')
    if surface.get_at((ship_x +r_ship.get_width(), ship_y+r_ship.get_height()))==(63, 87, 210, 255):
        print('you win')
    if lives == 0:
        pygame.quit()
    surface.blit(ship_background, (back_x,back_y))
    surface.blit(r_ship, (50, 100))
    pygame.display.update()
