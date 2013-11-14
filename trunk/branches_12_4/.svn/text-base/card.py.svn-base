import pygame
import os
import random
from image import *

class Card(object):

	def __init__(self, screen, diameter, image_file_path): 
		self.screen = screen
		self.diameter = diameter
		self.image_file_path = image_file_path
		self.photo_list = self.create_photo_list()
        # Where does this get used? --KOH
		#~ self.image_list = image_list
		
	def initial_card(self, points):
		"""
		randomly chooses integers and maps them to images which are then
		put on the left card
		"""

        # Consider using random.sample() --KOH
		card_list = []
		while len(card_list)<8: # see 37 --KOH
			a = random.randint(0, len(self.photo_list)-1)
			if a not in card_list:
				card_list.append(a)

		final_list = []
		for i in card_list:
			final_item = self.photo_list[i]
			final_list.append(final_item)
		
		self.place_images(final_list, points)
		return card_list
			
	def place_images(self, final_list, points):
		"""
		places images on the card
		takes in a list of 8 image paths and 8 locations and puts them on the card 
		"""
		for i in range(8): 
            # Please change this (8) into a class-level variable --KOH
			image_object = final_list[i]
			image = pygame.image.load(image_object.file_path)
            # Why can't these be stored as a property of the class --KOH
			imagerect = image.get_rect()
			reimage = pygame.transform.scale(image, image_object.size)
			self.screen.blit(reimage, points[i])

	
		
	def create_photo_list(self):
		"""
		Creates a list of all of the filepaths of the images that we would want to insert in the cards
		"""
		p_list = os.listdir('photos')
		photo_list = []
		for item in p_list:
			if item[len(item)-4:] == '.png':
				new_item = 'photos/' + item # use os.path.join() --KOH
				photo_list.append(Image(new_item,(100,100)))
		return photo_list
		

	def put_images_on_card(self, int_list, points_old, points_new):
		"""
		Inserts 8 images onto the card on the old card and 8 new images on the new card
		"""

		# final_list_old is the list of image objects that will be on the old card
		final_list_old = []
		for i in int_list:
			final_item_old = self.photo_list[i]
			final_list_old.append(final_item_old)

		# card_list is the list of integers representing indexes of the image file paths in the photo_list
		card_list = []
		b = random.choice(int_list)
		card_list.append(b)
		while len(card_list)<8:
			a = random.randint(0, len(self.photo_list)-1)
			if a not in int_list and a not in card_list:
				card_list.append(a)
		random.shuffle(card_list)

		final_list_new = []
		for i in card_list:
			final_item_new = self.photo_list[i]
			final_list_new.append(final_item_new)
			
		correct_image_object = self.photo_list[b]
		old_index = final_list_old.index(correct_image_object)
		new_index = final_list_new.index(correct_image_object)
		correct_file_path = final_list_old[old_index].file_path
		final_list_old.pop(old_index)
		final_list_old.insert(old_index, CorrectImage(correct_file_path))
		final_list_new.pop(new_index)
		final_list_new.insert(new_index, CorrectImage(correct_file_path))
			
		self.place_images(final_list_old, points_old)		
		self.place_images(final_list_new, points_new)
		return card_list
		

