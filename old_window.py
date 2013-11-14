import pygame
import os
import random
 
# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
 
pygame.init()
  
# Set the height and width of the screen
size=[1000,500]
screen=pygame.display.set_mode(size)
 
pygame.display.set_caption("Spot It!")
 
#Loop until the user clicks the close button.
done=False
 
#create our background image
background_position = [0,0]
background_image = pygame.image.load('Woodgrain.jpg').convert()

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

#create a list of all of the images within the folder 'photos'
cwd = os.getcwd()
photo_dir = cwd + '/trunk/photos'
p_list = os.listdir(photo_dir)
photo_list = []
for item in p_list:
	if item[len(item)-4:] == '.png':
		new_item = cwd + '/trunk/photos/' + item
		photo_list.append(new_item)

#define image points for left card (lc) and right card (rc)
lc_points = ([225,75],[75,225],[225,375],[375,225],[115,335],[335,115],[115,115],[335,335])
rc_points= ([725,75],[575,225],[725,375],[875,225],[615,335],[835,115],[615,115],[835,335])

#creates two lists of 8 random integers
card1_list = []
card2_list = []
for i in range(8):
    a = random.randint(0, 20)
    card1_list.append(a)
for i in range(8):
    a = random.randint(0, 20)
    card2_list.append(a)

 
# -------- Main Program Loop -----------#
while done==False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    #function to insert all images onto the card on the left
    def insert_left_card_images():
        for i in range(8):
            image = pygame.image.load(photo_list[card1_list[i]])
            imagerect = image.get_rect()
            reimage = pygame.transform.scale(image, (50,50))
            screen.blit(reimage, lc_points[i])

    #function to insert all images onto the card on the right
    def insert_right_card_images():
        for i in range(8):
            image = pygame.image.load(photo_list[card2_list[i]])
            imagerect = image.get_rect()
            reimage = pygame.transform.scale(image, (50,50))
            screen.blit(reimage, rc_points[i])

    # Set the screen background
    screen.blit(background_image, background_position)
 
    #draw circle placeholders for the cards
    pygame.draw.circle(screen, red, [250,250], 205, 0)
    pygame.draw.circle(screen, red, [750,250], 205, 0)
    pygame.draw.circle(screen, white, [250,250], 200, 0)
    pygame.draw.circle(screen, white, [750,250], 200, 0)

    #insert the images on the cards
    insert_left_card_images()
    insert_right_card_images()
    
    """
    #function to insert an image at a point on a card
    def imaging(file):
        name = file.strip('.png')
        image = pygame.image.load(file)
        imagerect = image.get_rect()
        name = pygame.transform.scale(image, (50,50))
    """

    
    """
    image1 = pygame.image.load('Sarah.png')
    image1rect = image1.get_rect()
    reimage1 = pygame.transform.scale(image1, (50,50))
    image2 = pygame.image.load('jeff.png')
    image2rect = image2.get_rect()
    reimage2 = pygame.transform.scale(image2, (50,50))
    for i in range(len(lc_points)):
        screen.blit(reimage1, lc_points[i])
    for i in range(len(rc_points)):
        screen.blit(reimage2, rc_points[i])
    """
    # Limit to 30 frames per second
    clock.tick(30)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()
