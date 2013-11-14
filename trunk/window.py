import pygame
from scoreboard import *
import initial_options_window
import end_options_window
import random
import time
from card import *
from image import *

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
				new_item = 'photos/' + item 
				self.photodic[i] = (Image(new_item,(100,100)))
				i+=1

	def click_space(self, index_old, index_new, points_old, points_new, location):
		rect1 = pygame.Rect(points_old[index_old],[100,100])
		rect2 = pygame.Rect(points_new[index_new],[100,100])
		if rect1.collidepoint(location) or rect2.collidepoint(location):
			return True
		else:
			return False
	
	def place_images(self, final_list, points):
		"""
		places images on the card
		takes in a list of 8 image paths and 8 locations and puts them on the card 
		"""
		for i in range(8): 
			image_object = final_list[i]
			image = pygame.image.load(image_object.file_path)
			imagerect = image.get_rect()
			reimage = pygame.transform.scale(image, image_object.size)
			self.screen.blit(reimage, points[i])
	
	def add_game_score(self, difficulty, name, score):
		if difficulty == 'Easy':
			old_file = open('easy_scores.txt')
			line_list = []
			for line in old_file:
				line_list.append(line)
			easy_file = open('easy_scores.txt', 'w')
			for entry in line_list:
				easy_file.write(entry)
			line1 = name + '\n'
			line2 = score + '\n'
			easy_file.write(line1)
			easy_file.write(line2)
		elif difficulty == 'Medium':
			old_file = open('medium_scores.txt')
			line_list = []
			for line in old_file:
				line_list.append(line)
			medium_file = open('medium_scores.txt', 'w')
			for entry in line_list:
				medium_file.write(entry)
			line1 = name + '\n'
			line2 = score + '\n'
			medium_file.write(line1)
			medium_file.write(line2)
		else:
			old_file = open('hard_scores.txt')
			line_list = []
			for line in old_file:
				line_list.append(line)
			hard_file = open('hard_scores.txt', 'w')
			for entry in line_list:
				hard_file.write(entry)
			line1 = name + '\n'
			line2 = score + '\n'
			hard_file.write(line1)
			hard_file.write(line2)
	
	def extract_high_scores(self, difficulty):
		if difficulty == 'Easy':
			easy_file = open('easy_scores.txt')
			word_list = []
			for line in easy_file:
				a = line.rstrip('\r\n')
				word_list.append(a)
		elif difficulty == 'Medium':
			medium_file = open('medium_scores.txt')
			word_list = []
			for line in medium_file:
				a = line.rstrip('\r\n')
				word_list.append(a)
		else:
			hard_file = open('hard_scores.txt')
			word_list = []
			for line in hard_file:
				a = line.rstrip('\r\n')
				word_list.append(a)
		
		master_list = []
		for i in range(len(word_list)/2):
			master_list.append((int(word_list[2*i+1]), word_list[2*i]))
		placeholder = []
		for score, player in master_list:
			placeholder.append(score)
		score_set = set(placeholder)
		score_set = list(score_set)
		score_set.sort()
		sorted_master_list = []
		for element in score_set:
			for pair in master_list:
				if pair[0] == element:
					sorted_master_list.append(pair)
		sorted_master_list.reverse()
		players = []
		scores = []
		for i in range(5):
			scores.append(sorted_master_list[i][0])
			players.append(sorted_master_list[i][1])
		return [players, scores]
		
	

class Background(object):
	def __init__(self, window, options_list):
		self.window = window
		
		#create our background image and set it as the background for the screen
		self.position = [0,0]
		self.image = pygame.image.load('utility_photos/Woodgrain.jpg').convert()
		
		self.bar = pygame.image.load('utility_photos/bar.png')
		self.barrect = self.bar.get_rect()
		
		# load the background image
		self.window.screen.blit(self.image, self.position)
		self.window.screen.blit(self.bar,[0,0])
		
		self.card_reimage([75,215])
		self.card_reimage([750,215])
		
		player_font = pygame.font.Font(None, 30)
		player_name = player_font.render(options_list[1], 1, (0,0,0))
		computer_name = player_font.render(options_list[2], 1, (0,0,0))
		self.window.screen.blit(player_name, [290,20])
		self.window.screen.blit(computer_name, [950,20])
		
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
	
	#Constructing the GUI from the initial_options_window file and retreiving the info from the GUI
	gui = initial_options_window.Options_Gui()
	gui.constructGui()
	#options_list = ['difficulty level', 'player name', 'computer name']
	options_list = gui.options_info
	
	#Setting the delay in miliseconds of the computer based on difficulty level
	if options_list[0] == 'Hard':
		delay_range = [2000, 2800]
	elif options_list[0] == 'Medium':
		delay_range = [3000, 3800]
	else:
		delay_range = [4000, 4700]
	#Setting the Event ID for the timer
	GAMETIMEREVENT = pygame.USEREVENT + 1
	pygame.time.set_timer(GAMETIMEREVENT, 1000)
	font = pygame.font.Font('Elronmonospace.ttf', 130)
	COMP_TIMER_EVENT = pygame.USEREVENT + 2
	game_time = 61
	
	#Loop until the user clicks the close button.
	while done==False:
		pygame.event.clear()
		bg = Background(game, options_list)

		for event in pygame.event.get(): # User did something
			if event.type == pygame.QUIT: # If user clicked close
				done=True # Flag that we are done so we exit this loop
			elif counter ==0:
				start = time.time()
				card1 = Card(game.photodic)
				image_info = card1.initial_cards()
				game.place_images(image_info.file_path_list_old, lc_points)
				game.place_images(image_info.file_path_list_new, rc_points)
				oldp = lc_points
				newp = rc_points
				counter += 1
				score = Score((70, 100))
				ltscore = font.render(str(score.leftscore), 1, (0,0,0))
				rtscore = font.render(str(score.rightscore), 1, (0,0,0))
				screen.blit(ltscore, [110,40])
				screen.blit(rtscore, [1250,40])
				computer_delay = random.randint(delay_range[0], delay_range[1])
				pygame.time.set_timer(COMP_TIMER_EVENT, int(computer_delay))
				pygame.display.flip()
			# Player
			elif event.type == pygame.MOUSEBUTTONDOWN and game.click_space(image_info.old_index, image_info.new_index, oldp, newp, event.pos): 
				if counter %2 == 0:
					oldp = lc_points
					newp = rc_points
					image_info = card1.put_images_on_card(image_info.int_list)
					game.place_images(image_info.file_path_list_old, oldp)
					game.place_images(image_info.file_path_list_new, newp)
				else:
					oldp = rc_points
					newp = lc_points
					image_info = card1.put_images_on_card(image_info.int_list)
					game.place_images(image_info.file_path_list_old, oldp)
					game.place_images(image_info.file_path_list_new, newp)
				score.left()
				ltscore = font.render(str(score.leftscore), 1, (0,0,0))
				if score.leftscore <= 9:
					screen.blit(ltscore, [110,40])
				else:
					screen.blit(ltscore, [68,40])
				if score.rightscore <= 9:
					screen.blit(rtscore, [1250,40])
				else:
					screen.blit(rtscore, [1203,40])				
				counter += 1
				if (game_time - (time.time() - start)) > 2:
					computer_delay = random.randint(delay_range[0], delay_range[1])
				else: 
					computer_delay = 3000
				pygame.time.set_timer(COMP_TIMER_EVENT, int(computer_delay))
				screen.blit(timer, [545,40])
				pygame.display.flip()
			# Computer Opponenet 
			elif event.type == GAMETIMEREVENT:
				time2 = (game_time - (time.time() - start))
				mins = int(time2/60)
				secs = time2 %60
				#print mins, secs
				timer = font.render("%d:%02d" % (mins, secs), 1, (0, 0, 0))
				timerrect = timer.get_rect(size = (500,200), center = (600,100))
				screen.blit(timer, [545,40])
				pygame.display.update([timerrect])
				if "%d:%02d" % (mins, secs) == '0:00':
					game.add_game_score(options_list[0], options_list[1],str(score.leftscore))
					info = game.extract_high_scores(options_list[0])
					player_names = info[0]
					scores = info[1]
					difficulty_level = options_list[0]
					win_lose = 'lose'
					if score.leftscore > score.rightscore:
						win_lose = 'win'
					end_gui = end_options_window.End_Gui()
					end_gui.constructGui(difficulty_level, player_names, scores, win_lose)
					if end_gui.command == 'play':
						score.leftscore = 0
						score.rightscore = 0
						counter = 0
						#~ pygame.time.set_timer(COMP_TIMER_EVENT, int(computer_delay))
						computer_delay = 5000
						pygame.display.flip()
						main()
					else:
						done = True
			elif event.type == COMP_TIMER_EVENT:
				if counter %2 == 0:
					oldp = lc_points
					newp = rc_points
					image_info = card1.put_images_on_card(image_info.int_list)
					game.place_images(image_info.file_path_list_old, oldp)
					game.place_images(image_info.file_path_list_new, newp)
				else:
					oldp = rc_points
					newp = lc_points
					image_info = card1.put_images_on_card(image_info.int_list)
					game.place_images(image_info.file_path_list_old, oldp)
					game.place_images(image_info.file_path_list_new, newp)
				score.right()
				rtscore = font.render(str(score.rightscore), 1, (0,0,0))				
				if score.leftscore <= 9:
					screen.blit(ltscore, [110,40])
				else:
					screen.blit(ltscore, [68,40])
				if score.rightscore <= 9:
					screen.blit(rtscore, [1250,40])
				else:
					screen.blit(rtscore, [1203,40])
				counter += 1
				if (game_time - (time.time() - start)) > 2:
					computer_delay = random.randint(delay_range[0], delay_range[1])
				else: 
					computer_delay = 3000
				pygame.time.set_timer(COMP_TIMER_EVENT, int(computer_delay))
				screen.blit(timer, [545,40])
				pygame.display.flip()
			#Timer Stuff

		# Limit to 30 frames per second
		clock.tick(1000)
		
	pygame.quit ()

if __name__ == '__main__':
	main()
