import pygame, time

def main():
	# Initialise screen
	pygame.init()
	screen = pygame.display.set_mode((400, 450))
	pygame.display.set_caption('Basic Pygame program')

	# Fill background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250, 250, 250))
	
	# Display some text
	font = pygame.font.Font(None, 36)

	# Blit everything to the screen
	screen.blit(background, (0, 0))
	pygame.display.flip()
	
	#Do time stuff
	GAMETIMEREVENT = pygame.USEREVENT + 1
	pygame.time.set_timer(GAMETIMEREVENT, 1000)
	
	done = False
	start = time.time()
	default_time = 10
	# Event loop
	while done==False: 
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done=True 
			elif event.type == GAMETIMEREVENT:
				time2 = (default_time - (time.time() - start))
				mins = int(time2/60)
				secs = time2 %60
				text = font.render("%d:%02d" % (mins, secs), 1, (10, 10, 10))
				textpos = text.get_rect()
				textpos.centerx = background.get_rect().centerx
				background.blit(text, textpos)
				screen.blit(background, (0, 0))
				pygame.display.flip()
				if "%d:%02d" % (mins, secs) == '0:00':
					done = True

if __name__ == '__main__': main()
