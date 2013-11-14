import pygame
from card import *

class Table(object):

	def __init__(self, screen, card_1_location, card_2_location):
		self.screen = screen
		self.card_1_location = card_1_location
		self.card_2_location = card_2_location

	def make_table_initial(self, points):

		card_image_path = 'utility_photos/Card_circle.png'
	
		#create one card with attributes: screen, diameter, and card image path
		card1 = Card(self.screen, 450, card_image_path)

		#insert the 2 cards
		image1 = pygame.image.load(card1.image_file_path)
		imagerect1 = image1.get_rect()
		reimage1 = pygame.transform.scale(image1, (card1.diameter,card1.diameter))
		self.screen.blit(reimage1, self.card_1_location)
		card_list = card1.inital_card(points)
		return card_list

		
	def make_new_table(self, int_list, points_new, points_old):

		card_image_path = 'utility_photos/Card_circle.png'
	
		#create two cards with attributes: screen, diameter, and card image path
		card1 = Card(self.screen, 450, card_image_path)
		card2 = Card(self.screen, 450, card_image_path)

		#insert the cards

		image1 = pygame.image.load(card1.image_file_path)
		imagerect1 = image1.get_rect()
		reimage1 = pygame.transform.scale(image1, (card1.diameter,card1.diameter))
		self.screen.blit(reimage1, self.card_1_location)

		image2 = pygame.image.load(card2.image_file_path)
		imagerect2 = image2.get_rect()
		reimage2 = pygame.transform.scale(image2, (card2.diameter,card2.diameter))
		self.screen.blit(reimage2, self.card_2_location)

		card1.put_old_images_on_card(int_list, points_old)
		int_list = card2.put_new_images_on_card(int_list, points_new)
		
		return int_list
