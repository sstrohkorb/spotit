from Tkinter import *

class End_Gui(object):
	
	def __init__(self, command = 'quit'):
		self.command = command
	
	def constructGui(self, difficulty_level, player_names, scores, win_lose):
		self.root = Tk()
		self.root.title('End of Game Options')
		self.root.geometry("290x425+550+200")
	
		logo = PhotoImage(file = "utility_photos/logo_small.gif")													
		self.label = Label(self.root, image=logo).grid(row=0, column = 2, columnspan = 10)	
		
		self.space = Label(self.root, text=" ").grid(row=1, column=0, columnspan = 10)
		
		if win_lose == 'win':
			self.win_lose = Label(self.root, text='YOU WON!').grid(row=2, column=0, columnspan = 14)
		else:
			self.win_lose = Label(self.root, text='SORRY, YOU LOST...').grid(row=2, column=0, columnspan = 14)
		
		#~ self.space = Label(self.root, text=" ").grid(row=2, column=0, columnspan = 10)
		
		self.player_name_label = Label(self.root, text= difficulty_level + " Level High Scores").grid(row=3, column=3, columnspan = 8)	
		
		for i in range(5):
			self.space = Label(self.root, text=" ").grid(row=2*i+4, column=0, columnspan = 10)	
			self.name = Label(self.root, text = player_names[i]).grid(row=2*i+5	, column = 0, columnspan = 4)
			self.score = Label(self.root, text = str(scores[i])).grid(row=2*i+5, column = 11, columnspan = 1)																
		
		self.space = Label(self.root, text=" ").grid(row=14, column=0, columnspan = 10)
		
		self.play_again_button = Button(self.root, text = "Play Again", command = self.play_again)
		self.play_again_button.grid(row = 15, column = 0, columnspan = 4)
		
		self.quit_button = Button(self.root, text = "Quit", command = self.quit_game)
		self.quit_button.grid(row = 15, column = 11, columnspan = 4)
		
		self.root.mainloop() 	
	
	def play_again(self):
		self.command = 'play'
		self.root.destroy()
	
	def quit_game(self):
		self.root.destroy()
	

#~ gui = End_Gui()
#~ player_names = ['Sarah Strohkorb', 'Jeff Hart', 'Keely Haverstock', 'Tanner Reid', 'Hedgehog']
#~ scores = ['120', '100', '80', '70', '68']
#~ win_lose = 'lose'
#~ gui.constructGui('Easy', player_names, scores, win_lose)
