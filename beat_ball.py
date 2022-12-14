import sys, pygame, random 

pygame.init()

Clock = pygame.time.Clock()

#Features of game entities
size = width, height = 500, 500
ball_size = (30, 25)
tile_size = (90, 20)
block_size = (100, 25)
ball_speed = [8, 5]
tile_speed = 10
black = 0, 0, 0
block_color = 255, 255, 255

screen = pygame.display.set_mode(size)

#Creating the ball
ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, ball_size)
ballrect = ball.get_rect()

#Creating the player-controlled tile
tile = pygame.image.load("tile.png")
tile = pygame.transform.scale(tile, tile_size)
tilerect = tile.get_rect(center = (tile_size[0] / 2, height))

#Creating blocks that the player will destroy to generate points

blocks = []
for i in range(2):
        for j in range(int(width / block_size[0])):
            block = pygame.image.load("1.png")
            block = pygame.transform.scale(block, block_size)
            blockrect = block.get_rect(center = (block_size[0] / 2 + block_size[0] * j, block_size[1] / 2 + block_size[1] * i))
            blocks.append((block, blockrect))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if len(blocks) == 0:
            sys.exit()

    ballrect = ballrect.move(ball_speed)

    #Ensure ball remains in the screen
    if ballrect.left < 0 or ballrect.right > width:
        ball_speed[0] = -ball_speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        ball_speed[1] = -ball_speed[1]

    #Collision between ball and top of tile
    if ballrect.bottom > tilerect.top and ((ballrect.right >= tilerect.left and ballrect.left <= tilerect.left) or (ballrect.left >= tilerect.left and ballrect.right <= tilerect.right) or (ballrect.left <= tilerect.right and ballrect.right >= tilerect.right)):
        ball_speed[1] = -ball_speed[1]

    #Collision between ball and left side of tile
    if (ball_speed[0] > 0):
        if (ballrect.right >= tilerect.left and ballrect.left < tilerect.left) and (ballrect.bottom >= tilerect.top and ballrect.bottom < height):
            print("hit3")
            ball_speed[0], ball_speed[1] = -ball_speed[0], -ball_speed[1]
    
    #Collision between ball and right side of tile
    if (ball_speed[0] < 0):
        if (ballrect.left <= tilerect.right and ballrect.right > tilerect.right) and (ballrect.bottom >= tilerect.top and ballrect.bottom < height):
            print("hit2")
            ball_speed[0], ball_speed[1] = -ball_speed[0], -ball_speed[1]

    #Block and ball collision
    for i in range(len(blocks)):

        #Collision between top of block and ball
        
        blkrect = blocks[i][1]
        if (ballrect.top <= blkrect.bottom and ballrect.bottom >= blkrect.top) and ((ballrect.right >= blkrect.left and ballrect.left <= blkrect.left) or (ballrect.left >= blkrect.left and ballrect.right <= blkrect.right) or (ballrect.left <= blkrect.right and ballrect.right >= blkrect.right)):
            blocks[i] = None
            ball_speed[1] = -ball_speed[1]
            print("hit4")

        #Collision between ball and left side of block
        if (ball_speed[0] > 0):
            if (ballrect.right >= blkrect.left and ballrect.left < blkrect.left) and (ballrect.top <= blkrect.bottom and ballrect.bottom >= blkrect.top):
                blocks[i] = None
                ball_speed[0] = -ball_speed[0]
                print("Hit1")
        
        #Collision between ball and right side of block
        if (ball_speed[0] < 0):
            if (ballrect.left <= blkrect.right and ballrect.right > blkrect.right) and (ballrect.top <= blkrect.bottom and ballrect.bottom >= blkrect.top):
                blocks[i] = None
                ball_speed[0]= -ball_speed[0]

    blocks = list(filter(lambda el : el is not None, blocks))

    #Player input
    key_states = pygame.key.get_pressed()
    if key_states[pygame.K_a]:
        tilerect = tilerect.move([-tile_speed, 0])
    if key_states[pygame.K_d]:
        tilerect = tilerect.move([tile_speed, 0])


    Clock.tick(10)
    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(tile, tilerect)

    #Creating blocks that the player will destroy to generate points
    for i in range(len(blocks)):
        blk = blocks[i]
        screen.blit(blk[0], blk[1])
        

    pygame.display.flip()

    

