from Tkinter import *

class Options_Gui(object):
	
	def __init__(self, options_info = ['Easy', 'Tanner', 'Kiefer']):
		self.options_info = options_info
	
	def constructGui(self):

		self.root = Tk()
		self.root.title('Game Options')
		self.root.geometry("290x425+550+200")
	
		logo = PhotoImage(file = "utility_photos/logo_small.gif")													
		self.label = Label(self.root, image=logo).grid(row=0, column = 2, columnspan = 10)								
		
		self.space = Label(self.root, text=" ").grid(row=1, column=0, columnspan = 10)									

		self.player_name_label = Label(self.root, text="What is your name?").grid(row=2, column=3, columnspan = 8)		
		
		self.player_name_entry = Entry(self.root)
		self.player_name_entry.grid(row=3, column=3, columnspan = 8)
		self.player_name_entry.insert(0,"Tanner")												
		self.player_name_entry.focus_set()
		
		self.space = Label(self.root, text=" ").grid(row=4, column=0, columnspan = 10)									
		
		self.player_name_label = Label(self.root, text="What is the computer's name?").grid(row=5, column=3, columnspan = 8)
		
		self.computer_name_entry = Entry(self.root)
		self.computer_name_entry.grid(row=6, column=3, columnspan = 8)
		self.computer_name_entry.insert(0,"Kiefer")													
		self.computer_name_entry.focus_set()
		
		self.space = Label(self.root, text=" ").grid(row=7, column=0, columnspan = 10)									

		self.difficulty_level = Label(self.root, text="Difficulty Level:").grid(row=8, column=4, columnspan = 6)		
		
		v = IntVar()
		value = 0
		self.level_list = ['Easy']
		self.easy_button = Radiobutton(self.root, text="Easy", variable=v, value=1, command = lambda: self.level_selection("Easy", self.level_list))
		self.easy_button.grid(row=9, column=5, columnspan = 2)	
		self.meduim_button = Radiobutton(self.root, text="Medium", variable=v, value=2, command = lambda: self.level_selection("Medium", self.level_list))
		self.meduim_button.grid(row=10, column=5, columnspan = 2)			
		self.hard_button = Radiobutton(self.root, text="Hard", variable=v, value=3, command = lambda: self.level_selection("Hard", self.level_list))
		self.hard_button.grid(row=11, column=5, columnspan = 2)				
		
		self.space = Label(self.root, text=" ").grid(row=12, column=0, columnspan = 10)									

		buttonPic = PhotoImage(file = "utility_photos/play_small.gif")
		self.playButton = Button(self.root, image = buttonPic, command=self.play)
		self.playButton.grid(row = 13, column = 6) 																		
		
		self.root.mainloop() 											
	
	def play(self):
		level = self.level_list[0]
		player_name = self.player_name_entry.get()
		computer_name = self.computer_name_entry.get()
		self.options_info = [level, player_name, computer_name]
		self.root.destroy()
		
		
	def level_selection(self, diff, level_list):
		level_list.append(diff)
		if len(level_list) > 1:
			level_list.pop(0)
		
#~ gui = Options_Gui()
#~ gui.constructGui()
