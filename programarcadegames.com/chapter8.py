# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
 
# Explanation video: http://youtu.be/vRB_983kUMc
 
import pygame, sys, os, random, math
from pygame.locals import *
 
# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
 
pygame.init()
  
# Set the width and height of the screen [width,height]
size = [700,500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

max_x  = screen.get_width() - 50
max_y  = screen.get_height() - 50
rect_x = random.randint(0, max_x)
rect_y = random.randint(0, max_y)

speed = .75 
change_x = 5 * speed 
change_y = 4 * speed 

r = 0 
b = 0
g = 0

font = pygame.font.Font(None, 22)

# -------- Main Program Loop -----------
while done == False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
  
  
    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
    # ######
     
 
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    # ######
    
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(black)
    
    # keep on screen
    if (rect_x > max_x):
        change_x = change_x * -1
    if (rect_x < 0):
        change_x = change_x * -1
    if (rect_y > max_y):
        change_y = change_y * -1        
    if (rect_y < 0):
        change_y = change_y * -1
        
    # change color
    if (r < 255 and b < 255 and g < 255):
        r += 1
        
    if (r == 255 and g < 255):
        g += 1

    if (g == 255 and b < 255):
        b += 1        
    
    if (b == 255 and r > 0): 
        r -= 1
        
    if (r == 0 and g > 0):
        g -= 1
        
    if (g == 0 and b > 0):
        b -= 1
        
    
        
    pygame.draw.rect(screen, (r, g, b), [rect_x, rect_y, 50, 50])
    rect_x += change_x
    rect_y += change_y
    
    rgb = "{}, {}, {}".format(r, g, b)
    text = font.render(rgb, True, white)
    screen.blit(text, [0,0])
    
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
     
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    
 
    # Limit to 30 frames per second
    clock.tick(30)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
