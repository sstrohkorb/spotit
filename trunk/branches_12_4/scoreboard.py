import pygame
on = (255,0,0)
off = (220,220,220)

def number(screen, colors, xaxis):	
	pygame.draw.rect(screen, colors[0], (60+xaxis,35,8,50), 0)
	pygame.draw.rect(screen, colors[1], (60+xaxis,95,8,50), 0)
	pygame.draw.rect(screen, colors[2], (124+xaxis,35,8,50), 0)
	pygame.draw.rect(screen, colors[3], (124+xaxis,95,8,50), 0)
	pygame.draw.rect(screen, colors[4], (72+xaxis,25,50,8), 0)
	pygame.draw.rect(screen, colors[5], (72+xaxis,85,50,8), 0)
	pygame.draw.rect(screen, colors[6], (72+xaxis,145,50,8), 0)

def nine(screen, xaxis):
	colors = (on, off, on, on, on, on, on)
	number(screen, colors, xaxis)

def eight(screen, xaxis):
	colors = (on, on, on, on, on, on, on)
	number(screen, colors, xaxis)

def seven(screen, xaxis):
	colors = (off, off, on, on, on, off, off)
	number(screen, colors, xaxis)

def six(screen, xaxis):
	colors = (on, on, off, on, on, on, on)
	number(screen, colors, xaxis)

def five(screen, xaxis):
	colors = (on, off, off, on, on, on, on)
	number(screen, colors, xaxis)

def four(screen, xaxis):
	colors = (on, off, on, on, off, on, off)
	number(screen, colors, xaxis)

def three(screen, xaxis):
	colors = (off, off, on, on, on, on, on)
	number(screen, colors, xaxis)

def two(screen, xaxis):
	colors = (off, on, on, off, on, on, on)
	number(screen, colors, xaxis)

def one(screen, xaxis):
	colors = (off, off, on, on, off, off, off)
	number(screen, colors, xaxis)
	
def colon(screen):
	red = (255,0,0)
	pygame.draw.circle(screen, red, (720,65), 10, 0)
	pygame.draw.circle(screen, red, (720,115), 10, 0)
#~ class scoreboard(object):
	#~ 
	#~ def __init__(self, oncolor=(255,0,0), offcolor=(255,200,200)):
		#~ self.oncolor = oncolor
		#~ self.offcolor = offcolor
		#~ 
	#~ def make_number(self):
		#~ pygame.draw.rect(screen, self.oncolor, (10,100,10,50), 0)
