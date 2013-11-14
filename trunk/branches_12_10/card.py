import pygame
import os
import random
from image import *

class Card(object):

	def __init__(self, photodictionary): 
		self.photo_list = photodictionary
        # Where does this get used? --KOH
		#~ self.image_list = image_list
		
	def initial_cards(self):
		"""
		randomly chooses integers and maps them to images which are then
		put on the left card
		"""

        # Consider using random.sample() --KOH
		card_list_1 = []
		while len(card_list_1)<8: # see 37 --KOH
			a = random.randint(0, len(self.photo_list)-1)
			if a not in card_list_1:
				card_list_1.append(a)

		final_list_old = []
		for i in card_list_1:
			final_item = self.photo_list[i]
			final_list_old.append(final_item)
			
			
		card_list_2= []
		b = random.choice(card_list_1)
		card_list_2.append(b)
		while len(card_list_2)<8:
			a = random.randint(0, len(self.photo_list)-1)
			if a not in card_list_1 and a not in card_list_2:
				card_list_2.append(a)
		random.shuffle(card_list_2)
		
		final_list_new = []
		for i in card_list_2:
			final_item = self.photo_list[i]
			final_list_new.append(final_item)
			
		correct_image_object = self.photo_list[b]
		old_index = final_list_old.index(correct_image_object)
		new_index = final_list_new.index(correct_image_object)
		
		New_Info = Card_Information(card_list_2, final_list_old, final_list_new, old_index, new_index)
		
		return New_Info
		

	def put_images_on_card(self, int_list):
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
		
		New_Info = Card_Information(card_list, final_list_old, final_list_new, old_index, new_index)

		return New_Info
		
class Card_Information(object):
	def __init__(self, int_list, file_path_list_old, file_path_list_new, old_index, new_index):
		self.int_list = int_list
		self.file_path_list_old = file_path_list_old
		self.file_path_list_new = file_path_list_new
		self.old_index = old_index
		self.new_index = new_index

