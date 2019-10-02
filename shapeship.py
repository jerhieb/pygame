import pygame, random
pygame.init()
clock = pygame.time.Clock()
ship = pygame.image.load('spaceship thrust.png')
bullet = pygame.image.load('Bullet.png')
bullet = pygame.transform.rotate(bullet, 90)
surface = pygame.display.set_mode((800, 800))
anders_ship = pygame.image.load("Anders jet.png")
ship_x = 50
ship_y = 50
anders_x = 400
anders_y = 500
anders_xv = 1
anders_yv = 1
ship_xv = 0
ship_yv = 0
bullet_tracker = [[0,0]]
a_ships=[]
a_ships_change = 1
ay_ships_change = 1
last_direction = 'up'
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                last_direction = 'right'
                ship_xv = 1
            if event.key == pygame.K_LEFT:
                last_direction = 'left'
                ship_xv = -1
            if event.key == pygame.K_UP:
                last_direction = 'up'
                ship_yv = -1
            if event.key == pygame.K_DOWN:
                last_direction = 'down'
                ship_yv = 1
            if event.key == pygame.K_f:
                bullet_location = [ship_x, ship_y]
                bullet_tracker.append(bullet_location)
                
        if event.type ==pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                
                ship_xv = 0
            if event.key == pygame.K_LEFT:
                ship_xv = 0
            if event.key == pygame.K_UP:
                ship_yv = 0
            if event.key == pygame.K_DOWN:
                ship_yv = 0
    surface.fill((102, 240, 235))
    for i in bullet_tracker:
        if i[1]<0:
            bullet_tracker.remove(i)
        i[1] = i[1]-2
        
        bull = surface.blit(bullet, i)
        
    clock.tick()
    ship_x += ship_xv
    ship_y += ship_yv
    if ship_x < 0:
        ship_x = 800
    if ship_y >800:
        ship_y = 0
    if ship_x>800:
        ship_x=0
    if ship_y<0:
        ship_y = 800
    anders_x +=anders_xv
    anders_y += anders_yv
    if anders_x<0 or anders_x>780:
        anders_xv = -anders_xv
    if anders_y<0 or anders_y>700:
        anders_yv = -anders_yv
    if  len(a_ships)<20:
        a_ships.append([random.randint(0,800), random.randint(0,800)])
    
    for i in (a_ships):
        a_ship=surface.blit(anders_ship, [i[0], i[1]])
        if i[0]<0 or i[0]>780:
            a_ships_change= -a_ships_change
        if i[1]<0 or i[1]>780:
            ay_ships_change=-ay_ships_change
        i[1]=i[1]-ay_ships_change
        i[0]=i[0]-a_ships_change
    if last_direction == 'right':
        shipy = pygame.transform.rotate(ship, 270)
    if last_direction == 'up':
        shipy = pygame.transform.rotate(ship, 0)
    if last_direction == 'left':
        shipy = pygame.transform.rotate(ship, 90)
    if last_direction == 'down':
        shipy = pygame.transform.rotate(ship, 180)
    our_ship = surface.blit(shipy, (ship_x, ship_y))
    if our_ship.colliderect(a_ship):
        pygame.quit()
    
    for i in a_ships:
        #print(i)
        '''
        if a_ships[i].colliderect(bull):
            a_ships.remove(i)
        '''
    
    pygame.display.update()