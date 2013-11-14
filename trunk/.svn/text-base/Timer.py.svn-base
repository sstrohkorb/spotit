import time

class Getcountdown(object):
	
	def __init__(self, set_time=120):
		self.set_time = set_time
		self.timer(set_time)
		
		
	def timer(self, set_time):
		start = time.time()
		running = True
		current_time = []
		while running:
			if time.time() - start >= set_time:
				running = False
				return False
			else:
				time2 = (set_time - (time.time() - start))
				mins = int(time2/60)
				secs = time2 %60
				current_time.append("%d:%02d" % (mins, secs))
				self.get_current_time(current_time)
	
	def get_current_time(self,time):
		print time[len(time)-1]
	
Timer = Getcountdown(2)

