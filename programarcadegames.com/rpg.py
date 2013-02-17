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

pygame.init()

# Set the width and height of the screen [width,height]
size=[800,600]
screen=pygame.display.set_mode(size)

pygame.display.set_caption("RPG")

#Loop until the user clicks the close button.
done=False

background = pygame.Surface(screen.get_size())
background = background.convert()

# Fill the screen with a black background
background.fill(black)

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

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

    pygame.draw.line(screen, green, [0,0], [100,100], 5)

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
