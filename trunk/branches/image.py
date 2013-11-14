import pygame
from widget import *

class Image(Widget):

	def __init__(self, evManager, file_path, size=(50,50), 		
		container=None, onClickEvent=None):
		Widget.__init__(self, evManager, container)

		self.file_path = file_path
		self.size = size

		#self.font = pygame.font.Font(None, 30)
		#self.text = text
		#self.image = self.font.render( self.text, 1, (255,0,0))
		#self.rect  = self.image.get_rect()

		self.onClickEvent = onClickEvent

    #----------------------------------------------------------------------
	def update(self):
		if not self.dirty:
			return

		if self.focused:
			color = (255,255,0)
		else:
			color = (255,0,0)
		self.image = self.font.render( self.text, 1, color)
        #self.rect  = self.image.get_rect()

		self.dirty = 0

    #----------------------------------------------------------------------	
	def Connect(self, eventDict):
		for key,event in eventDict.iteritems():
			try:
				self.__setattr__( key, event )
			except AttributeError:
				print "Couldn't connect the ", key
				pass


    #----------------------------------------------------------------------
	def Click(self):
		self.dirty = 1
		if self.onClickEvent:
			self.evManager.Post( self.onClickEvent )

    #----------------------------------------------------------------------
	def Notify(self, event):
		if isinstance( event, GUIPressEvent ) and self.focused:
			self.Click()

		elif isinstance( event, GUIClickEvent ) \
			and self.rect.collidepoint( event.pos ):
			self.Click()

		elif isinstance( event, GUIMouseMoveEvent ) \
			and self.rect.collidepoint( event.pos ):
			ev = GUIFocusThisWidgetEvent(self)
			self.evManager.Post( ev )

		Widget.Notify(self,event)

"""
	def __init__(self, file_path, size=(50,50)):
		super(Button,self).__init__()
		self.file_path = file_path
		self.size = size
"""
