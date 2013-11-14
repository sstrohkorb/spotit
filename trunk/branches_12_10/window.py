import pygame
from scoreboard import *
from card import *
from image import *
from Timer import *
#~ from initial_options_window import *

class Window(object):
	def __init__(self, size=[1440,820]):
		self.size = size
		self.photodic = {}
		self.correct = []
		
		# Set the height and width of the screen
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption("Spot It!")
		
		"""
		Creates a dictionary of all of the filepaths of the images that we would want to insert in the cards
		"""
		p_list = os.listdir('photos')
		i = 0
		for item in p_list:
			if item[len(item)-4:] == '.png':
				new_item = 'photos/' + item # use os.path.join() --KOH
				self.photodic[i] = (Image(new_item,(100,100)))
				i+=1

	def click_space(self, index_old, index_new, points_old, points_new, location):
		rect1 = pygame.Rect(points_old[index_old],[100,100])
		rect2 = pygame.Rect(points_new[index_new],[100,100])
		if rect1.collidepoint(location) or rect2.collidepoint(location):
			return True
		else:
			return False
	def even():
		oldp = lc_points
		newp = rc_points
		image_info = card1.put_images_on_card(image_info.int_list)
		game.place_images(image_info.file_path_list_old, oldp)
		game.place_images(image_info.file_path_list_new, newp)	
		
	def place_images(self, final_list, points):
		"""
		places images on the card
		takes in a list of 8 image paths and 8 locations and puts them on the card 
		"""
		for i in range(8): 
            # Please change this (8) into a class-level variable --KOH
			image_object = final_list[i]
#		if type(image_object) == 'CorrectImage':
#				self.correct = [i, points[i]]
			image = pygame.image.load(image_object.file_path)
            # Why can't these be stored as a property of the class --KOH
			imagerect = image.get_rect()
			reimage = pygame.transform.scale(image, image_object.size)
			self.screen.blit(reimage, points[i])
	

class Background(object):
	def __init__(self, window):
		self.window = window
		
		#create our background image and set it as the background for the screen
		self.position = [0,0]
		self.image = pygame.image.load('utility_photos/Woodgrain.jpg').convert()
		
		self.bar = pygame.image.load('utility_photos/bar.png')
		self.barrect = self.bar.get_rect()
		
		# load the background image
		window.screen.blit(self.image, self.position)
		window.screen.blit(self.bar,[0,0])
		
		self.card_reimage([75,215])
		self.card_reimage([750,215])
		
	def card_reimage(self, location):
		card_image_path = 'utility_photos/Card_circle.png'
		card1 = pygame.image.load(card_image_path)
		imagerect1 = card1.get_rect()
		reimage1 = pygame.transform.scale(card1, (600,600))
		self.window.screen.blit(reimage1, location)


def main():
	# Initialize the pygame modules
	pygame.init()
	
	game = Window()
	
	done = False
	
	# Used to manage how fast the screen updates
	clock=pygame.time.Clock()
	
	#set up a counter
	counter = 0
	lc_points = ([325,275],[135,470],[325,650],[500,450],[200,345],[450,345],[200,590],[450,590])
	rc_points = ([1000,275],[810,470],[1000,650],[1175,450],[875,345],[1125,345],[875,590],[1125,590])
	
	screen = game.screen

	
	
	#Loop until the user clicks the close button.
	while done==False: # ``not done'' --KOH
		# instantiate background
		bg = Background(game)
		
		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				done=True # Flag that we are done so we exit this loop

			elif counter ==0:#event.type == pygame.MOUSEBUTTONDOWN and 
				card1 = Card(game.photodic)
				image_info = card1.initial_cards()
				game.place_images(image_info.file_path_list_old, lc_points)
				game.place_images(image_info.file_path_list_new, rc_points)
				oldp = lc_points
				newp = rc_points
				counter += 1
				pygame.display.flip()
				#~ Timer = Getcountdown()
				#~ Timer.timer(10)
				scoreImage = Score((40, 50))
				#~ scoreImage.reRender()
				#~ scoreImage.draw()
				#~ scoreImage.add(ScoreGroup)
			elif event.type == pygame.MOUSEBUTTONDOWN and game.click_space(image_info.old_index, image_info.new_index, oldp, newp, event.pos):
				if counter %2 == 0:
					game.even()
				else:
					oldp = rc_points
					newp = lc_points
					#~ if game.click_space(old_index, new_index, oldp, newp, event.pos):
					image_info = card1.put_images_on_card(image_info.int_list)
					game.place_images(image_info.file_path_list_old, oldp)
					game.place_images(image_info.file_path_list_new, newp)
				scoreImage.right()
				print type(scoreImage)
				#~ game.screen.blit(scoreImage)  
				#~ scoreImage.reRender()
				#print scoreImage.rightscore
				counter += 1
				#~ scoreImage.left()
				#~ sprite.draw()
				pygame.display.flip()

		# Limit to 30 frames per second
		clock.tick(100)
		
		# Go ahead and update the screen with what we've drawn.
		#~ pygame.display.flip()
		
	pygame.quit ()

if __name__ == '__main__':
	main()