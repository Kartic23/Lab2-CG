import sys
import pygame

from core.input import Input


class Base(object):
    """Basic window"""
    def __init__(self, screenSize=(650, 650)):
        
        """initialize all pygame modules"""
        pygame.init()
 
        # indicate rendering details
        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL
        # initialize buffers to perform antialiasing
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        # use a core OpenGL profile for cross-platform compatibility
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE
        )
        # create and display the window
        self.screen = pygame.display.set_mode(screenSize, displayFlags)

        # set the text that appears in the title bar of the window
        pygame.display.set_caption("Kartic Premgi 71379")
        # determine if main loop is active
        self.running = True
        # manage time-related data and operations
        self.clock = pygame.time.Clock()
        # manage user input
        self.input = Input()
        

    # implement by extending class
    def initialize(self):
        pass

    def update(self):
        pass
        

    def run(self):
        ## startup ##
        self.initialize()

        ## main loop ##
        while self.running:
            ## process input ##
            self.input.update()
            if self.input.quit:
                self.running = False
                
                
            ## update ##
            self.update()

            ## render ##
            # display image on screen
            pygame.display.flip()
            # pause if necessary to achieve 60 FPS
            self.clock.tick(60)

   

        ## shutdown ##
        pygame.quit()
        sys.exit()
