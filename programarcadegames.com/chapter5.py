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
blue     = (   0,   0, 255)
 
pygame.init()
  
# Set the width and height of the screen [width,height]
size=[700,500]
screen=pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
#Loop until the user clicks the close button.
done=False
 
# Used to manage how fast the screen updates
clock=pygame.time.Clock()
 
# -------- Main Program Loop -----------
while done==False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
  
  
    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
     
 
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
     
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(white)

    pygame.draw.line(screen, green, [0,0], [100,100], 5)
    pygame.draw.line(screen, red,   [110,0], [100,200], 5)
    pygame.draw.line(screen, black, [0,110], [200,100], 5)
    
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen, blue, [10, 10 + y_offset], [100, 110 + y_offset], 5)
        
    for y_offset in range(0, 100, 5):
        pygame.draw.line(screen, blue, [10 + y_offset, 10], [200, 210 + y_offset], 1)
        pygame.draw.line(screen, red, [10 + y_offset, 100 - y_offset], [400, 410 + y_offset], 1)
        
    # ruler marks
    font = pygame.font.Font(None, 22)
    for offset in range(0, screen.get_width(), 100):
        text = font.render(str(offset), True, (255, 0, 255))
        
        # horizontal
        pygame.draw.line(screen, black, [offset, 0], [offset, 5], 4)
        screen.blit(text, [offset, 0])
        
        # vertical
        pygame.draw.line(screen, black, [0, offset], [5, offset], 4)
        screen.blit(text, [0, offset])
        
    # complex offsets 
    for i in range(200):   
        radians_x = i/20
        radians_y = i/6
         
        x = int( 75 * math.sin(radians_x)) + 300
        y = int( 75 * math.cos(radians_y)) + 200
         
        pygame.draw.line(screen,black,[x,y],[x+5,y], 2)
        
    # text 
    # Select the font to use. Default font, 25 pt size.
    font = pygame.font.Font(None, 25)
     
    # Render the text. "True" means anti-aliased text. 
    # Black is the color. The variable black was defined
    # above as a list of [0,0,0]
    # Note: This line creates an image of the letters, 
    # but does not put it on the screen yet.
    text = font.render("My text", True, black)
     
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [300,50])
    
    
        
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
     
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 20 frames per second
    clock.tick(20)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
