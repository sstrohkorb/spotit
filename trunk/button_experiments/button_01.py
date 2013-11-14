import pygame
from pygame.locals import *

class MyButton:
    """Button class based on the
    template method pattern."""
    
    def __init__(self, x, y, w, h):
        self.rect = Rect(x, y, w, h)
    def containsPoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def draw(self, surface):
        # You could of course use pictures here.
        # This method could also be implemented
        # by subclasses.
        #~ pygame.draw.rect(
            #~ surface,
            #~ (100,100,100), #gray
            #~ self.rect,
            #~ )
		x, y, w, h = self.rect
		image = pygame.image.load('Tanner.png')
		#~ imagerect = image.get_rect()
		reimage = pygame.transform.scale(image, (w , h))
		surface.blit(reimage, (x, y))
    def do(self):
        print "Implement in subclasses"

class BlueButton(MyButton):
    def __init__(self, x, y, w, h, app):
        # This is how you call the superclass init
        MyButton.__init__(self, x, y, w, h)
        self.app = app
    def do(self):
        self.app.setColor(SimpleUI.BLUE)
        
class RedButton(MyButton):
    def __init__(self, x, y, w, h, app):
        MyButton.__init__(self, x, y, w, h)
        self.app = app
    def do(self):
        self.app.setColor(SimpleUI.RED)

# The MyButton class is also used as a base for the
# colored area in the program. Here the do method
# does nothing. The draw method is overridden.

class ColorArea(MyButton):
    def __init__(self, x, y, w, h):
        MyButton.__init__(self, x, y, w, h)
        self.color = SimpleUI.BLUE
    def do(self):
        None
    def draw(self, surface):
        # by subclasses.
        pygame.draw.rect(
            surface,
            self.color,
            self.rect,
            )
    def setColor(self, color):
        self.color = color
        
class SimpleUI:
    
    RED = (255,0,0)
    BLUE = (0,0,255)

    def __init__(self):
        # Initialize PyGame
        pygame.init()
        pygame.display.set_caption("Simple UI")
        self.screen = pygame.display.set_mode((640,480))
        self.screen.fill((255,255,255))
        self.buttons = []
        self.addButton(BlueButton(20, 20, 100, 50, self))
        self.addButton(RedButton(20, 90, 100, 50, self))
        self.colorArea = ColorArea(140, 20, 400, 400)
        self.addButton(self.colorArea)
        
    def addButton(self, button):
        self.buttons = self.buttons + [button]
        
    def setColor(self, color):
        self.colorArea.setColor(color)
        
    def run(self):
        # Run the event loop
        self.loop()
        # Close the Pygame window
        pygame.quit()
    
    def loop(self):
        exit = False
        while not exit:
            exit = self.handleEvents()
            self.draw()

    def handleEvents(self):
            exit = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit = True
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit = True
                elif event.type == MOUSEBUTTONDOWN:
                    self.handleMouseDown(pygame.mouse.get_pos())
            return exit

    def handleMouseDown(self, (x, y)):
        for button in self.buttons:
            if (button.containsPoint(x, y)):
                button.do()
 
    def draw(self):
        for button in self.buttons:
            button.draw(self.screen)
        pygame.display.update()
            
# Start the program
SimpleUI().run()
