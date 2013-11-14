import pygame

class Widget(pygame.sprite.Sprite):
	def __init__(self, evManager, container=None):
		pygame.sprite.Sprite.__init__(self)

		#self.evManager = evManager
		#self.evManager.RegisterListener(self)

		self.container = container
		self.focused = 0
		self.dirty = 1

    #----------------------------------------------------------------------
	def SetFocus(self, val):
		self.focused = val
		self.dirty = 1

    #----------------------------------------------------------------------
	def kill(self):
		self.container = None
		del self.container
		pygame.sprite.Sprite.kill(self)

    #----------------------------------------------------------------------
	def Notify(self, event):
		if isinstance( event, GUIFocusThisWidgetEvent ) \
			and event.widget is self:
			self.SetFocus(1)

		elif isinstance( event, GUIFocusThisWidgetEvent ) \
			and self.focused:
			self.SetFocus(0)

