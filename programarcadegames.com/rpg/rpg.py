# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/


import pygame, sys, os, random, math
from pygame.locals import *

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)



class Tile(pygame.sprite.Sprite):
     
    def setGraphic(self, tilex, tiley, tilewidth, tileheight, x, y, width, height):
        global full_image
 
        self.image = pygame.Surface([width, height])

        self.image.blit(full_image, (0,0), (tilex,tiley,tilewidth,tileheight))
         
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x  
        self.image.set_colorkey(black)

class Grass(Tile):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        width  = 32
        height = 32
        tilex  = 32 * 1
        tiley  = 32 * 23
        self.setGraphic(tilex, tiley, width, height, x, y, width, height)

class River(Tile):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        width  = 64
        height = 32
        tilex  = 32 * 21
        tiley  = 32 * 17
        self.setGraphic(tilex, tiley, width, height, x, y, width, height)

pygame.init()


# Set the width and height of the screen [width,height]
size=[640,480]
screen=pygame.display.set_mode(size)

pygame.display.set_caption("RPG")

#Loop until the user clicks the close button.
done=False

full_image = pygame.image.load("terrain_atlas.png").convert()
background = pygame.Surface(screen.get_size())
background = background.convert()

# Fill the screen with a black background
background.fill(black)

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

wall_list = pygame.sprite.Group()
for row in range(screen.get_width()//32):
    for col in range(screen.get_height()//32):
        wall = Grass(row * 32, col * 32)
        wall_list.add(wall)

wall = River(32, 32)
wall_list.add(wall)
    

# -------- Main Program Loop --------------------------------------------------
while done==False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
    # -------------------------------------------------------------------------
    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

    

    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
    # -------------------------------------------------------------------------
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(white)


    wall_list.draw(screen)
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # -------------------------------------------------------------------------

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(20)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
