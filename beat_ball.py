import sys, pygame

pygame.init()

Clock = pygame.time.Clock()
size = width, height = 500, 500
ball_size = (30, 25)
tile_size = (90, 20)
ball_speed = [8, 5]
tile_speed = 10
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, ball_size)
ballrect = ball.get_rect()


tile = pygame.image.load("tile.png")
tile = pygame.transform.scale(tile, tile_size)
tilerect = tile.get_rect(center = (tile_size[0] / 2, height))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(ball_speed)

    #Ensure ball remains in the screen
    if ballrect.left < 0 or ballrect.right > width:
        ball_speed[0] = -ball_speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        ball_speed[1] = -ball_speed[1]

    #Collision between ball and top of tile
    if ballrect.bottom > tilerect.top and ((ballrect.right >= tilerect.left and ballrect.left <= tilerect.left) or (ballrect.left >= tilerect.left and ballrect.right <= tilerect.right) or (ballrect.left <= tilerect.left and ballrect.right >= tilerect.right)):
        ball_speed[1] = -ball_speed[1]

    #Collision between ball and left side of tile
    if (ball_speed[0] > 0):
        if (ballrect.right >= tilerect.left and ballrect.left < tilerect.left) and (ballrect.bottom >= tilerect.top and ballrect.bottom <= height):
             ball_speed[0], ball_speed[1] = -ball_speed[0], -ball_speed[1]
    
    #Collision between ball and right side of tile
    if (ball_speed[0] < 0):
        if (ballrect.left <= tilerect.right and ballrect.right > tilerect.right) and (ballrect.bottom >= tilerect.top and ballrect.bottom <= height):
             ball_speed[0], ball_speed[1] = -ball_speed[0], -ball_speed[1]


    key_states = pygame.key.get_pressed()
    if key_states[pygame.K_a]:
        tilerect = tilerect.move([-tile_speed, 0])
    if key_states[pygame.K_d]:
        tilerect = tilerect.move([tile_speed, 0])

    Clock.tick(40)
    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(tile, tilerect)
    pygame.display.flip()

    

