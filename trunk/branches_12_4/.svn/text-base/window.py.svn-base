import pygame
import scoreboard
from table import *

class Window(object):

	def __init__(self, size=[1440,820]):
		self.size = size

	def constructWindow(self):
		"""
		This function sets up the screen; it creates options and table objects. This is where everything happens.
		"""
		
		####  SARAH AND JEFF!! 
		####  dont worry all the colors are temporary :)
		
		
		
		
		
		#Initialize the pygame modules		
		pygame.init()

		# Set the height and width of the screen
		screen=pygame.display.set_mode(self.size)
		pygame.display.set_caption("Spot It!")
 
		#create our background image and set it as the background for the screen
		background_position = [0,0]
		background_image = pygame.image.load('utility_photos/Woodgrain.jpg').convert()
		
		bar = pygame.image.load('utility_photos/bar.png')
		barrect = bar.get_rect()
		#Loop until the user clicks the close button.
		done=False

		# Used to manage how fast the screen updates
		clock=pygame.time.Clock()
		
		#set up a counter
		counter = 0
		lc_points = ([325,275],[135,450],[325,650],[500,450],[200,345],[450,345],[200,590],[450,590])
		rc_points = ([1000,275],[810,450],[1000,650],[1175,450],[875,345],[1125,345],[875,590],[1125,590])

		while done==False: # ``not done'' --KOH
			for event in pygame.event.get(): # User did something
				if event.type == pygame.QUIT: # If user clicked close
					done=True # Flag that we are done so we exit this loop

			#load the background image
			screen.blit(background_image, background_position)
			screen.blit(bar,[0,0])
			
			scoreboard.one(screen,14)
			scoreboard.two(screen,96)
			scoreboard.three(screen,479)
			scoreboard.four(screen,561)
			scoreboard.five(screen,689)
			scoreboard.six(screen,771)
			scoreboard.seven(screen,1149)
			scoreboard.nine(screen,1231)
			scoreboard.colon(screen)
			
			#~ number = scoreboard()
			#~ number.make_number()
			if event.type == pygame.MOUSEBUTTONDOWN:

				#create a table with the attributes of card positions
				if counter == 0:
					table1 = Table(screen, [75,215], [750,215])
					int_list = table1.make_table_initial(lc_points)
				if counter %2 == 0:
					table1 = Table(screen, [750,215], [75,215])
					#~ table1.keep_rc(int_list)
					int_list = table1.make_new_table(int_list, lc_points, rc_points)
				else:
					table1 = Table(screen, [750,215], [75,215])
					int_list = table1.make_new_table(int_list, rc_points, lc_points)
				
				counter += 1
							# Limit to 30 frames per second
				#~ clock.tick(30)
				pygame.display.flip()
			else:
				pass
			
			#print counter
			# Limit to 30 frames per second
			clock.tick(100)
			

 
    		# Go ahead and update the screen with what we've drawn.
			#~ pygame.display.flip()
						
     
		pygame.quit ()


# Surround in if __name__ == '__main__': --KOH
game = Window()
game.constructWindow()
