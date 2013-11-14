import pygame
import os
import random
from image import *

class Card(object):

	def __init__(self, screen, diameter, image_file_path): #, image_list):
		self.screen = screen
		self.diameter = diameter
		self.image_file_path = image_file_path 
        # Where does this get used? --KOH
		#~ self.image_list = image_list
		
	def inital_card(self, points):
		"""
		randomly chooses integers and maps them to images which are then
		put on the left card
		"""
		photo_list = self.create_photo_list()
        # Is it really necessary to create the list anew every time? --KOH

        # Consider using random.sample() --KOH
		card_list = []
		while len(card_list)<8: # see 37 --KOH
			a = random.randint(0, len(photo_list)-1)
			if a not in card_list:
				card_list.append(a)

		final_list = []
		for i in card_list:
			final_item = photo_list[i]
			final_list.append(final_item)
		
		# places images on the card
		for i in range(8): 
            # Please change this (8) into a class-level variable --KOH
			image_object = final_list[i]
			image = pygame.image.load(image_object.file_path)
            # Why can't these be stored as a property of the class --KOH
			imagerect = image.get_rect()
			reimage = pygame.transform.scale(image, image_object.size)
			self.screen.blit(reimage, points[i])
		return card_list
	
		
	def create_photo_list(self):
		"""
		Creates a list of all of the filepaths of the images that we would want to insert in the cards
		"""
		p_list = os.listdir('photos')
		photo_list = []
		for item in p_list:
			if item[len(item)-4:] == '.png':
				new_item = 'photos/' + item # use os.path.join() --KOH
				photo_list.append(Image(new_item,(50,50)))
		return photo_list
		

	def put_old_images_on_card(self, int_list, points):
		"""
		Inserts 8 images onto the card on the left
		"""
		#defines a list of all the pathnames of the images
		photo_list = self.create_photo_list()

		final_list = []
		for i in int_list:
			final_item = photo_list[i]
			final_list.append(final_item)

        # This code looks real familiar ... --KOH
		for i in range(8): # see 37 --KOH
			image_object = final_list[i]
			image = pygame.image.load(image_object.file_path)
			imagerect = image.get_rect()
			reimage = pygame.transform.scale(image, image_object.size)
			self.screen.blit(reimage, points[i])
					

    # This needs to be made modular. --KOH
	def put_new_images_on_card(self, int_list, points):
		"""
		Inserts 8 images onto the card on the right
		"""
		#defines a list of all the pathnames of the images
		photo_list = self.create_photo_list()

		card_list = []
		b = random.choice(int_list)
		card_list.append(b)
		while len(card_list)<8:
			a = random.randint(0, len(photo_list)-1)
			if a not in int_list and a not in card_list:
				card_list.append(a)

		final_list = []
		for i in card_list:
			final_item = photo_list[i]
			final_list.append(final_item)
		#define image points 

		for i in range(8):
			image_object = final_list[i]
			image = pygame.image.load(image_object.file_path)
			imagerect = image.get_rect()
			reimage = pygame.transform.scale(image, image_object.size)
			self.screen.blit(reimage, points[i])
		return card_list
		

