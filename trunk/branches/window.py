import pygame
from table import *

class Window(object):

	def __init__(self, size=[1000,500]):
		self.size = size

	def constructWindow(self):
		"""
		This function sets up the screen; it creates options and table objects. This is where everything happens.
		"""
		
		#Initialize the pygame modules		
		pygame.init()

		# Set the height and width of the screen
		screen=pygame.display.set_mode(self.size)
		pygame.display.set_caption("Spot It!")
 
		#create our background image and set it as the background for the screen
		background_position = [0,0]
		background_image = pygame.image.load('utility_photos/Woodgrain.jpg').convert()
		
		#Loop until the user clicks the close button.
		done=False

		# Used to manage how fast the screen updates
		clock=pygame.time.Clock()
		
		#set up a counter
		counter = 0
		lc_points = ([225,75],[335,115],[375,225],[335,335],[225,375],[115,335],[75,225],[115,115])
		rc_points = ([725,75],[835,115],[875,225],[835,335],[725,375],[615,335],[575,225],[615,115])
		#rc_points = ([725,75],[575,225],[725,375],[875,225],[615,335],[835,115],[615,115],[835,335])

		while done==False:
			for event in pygame.event.get(): # User did something
				if event.type == pygame.QUIT: # If user clicked close
					done=True # Flag that we are done so we exit this loop

			#load the background image
			screen.blit(background_image, background_position)

			if event.type == pygame.MOUSEBUTTONDOWN:

				#create a table with the attributes of card positions
				if counter == 0:
					table1 = Table(screen, [25,25], [525,25])
					int_list = table1.make_table_initial(lc_points)
				if counter %2 == 0:
					table1 = Table(screen, [525,25], [25,25])
					#~ table1.keep_rc(int_list)
					int_list = table1.make_new_table(int_list, lc_points, rc_points)
				else:
					table1 = Table(screen, [525,25], [25,25])
					int_list = table1.make_new_table(int_list, rc_points, lc_points)
				
				counter += 1
							# Limit to 30 frames per second
				#~ clock.tick(30)
				pygame.display.flip()
			

			else:
				pass
			
			
			# Limit to 30 frames per second
			clock.tick(30)
			


 
    		# Go ahead and update the screen with what we've drawn.
			#~ pygame.display.flip()
						
     
		pygame.quit ()



game = Window()
game.constructWindow()

		



