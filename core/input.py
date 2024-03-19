import pygame

class Input(object):
    """Manages the users commands"""
    def __init__(self) -> None:
        """User terminated?"""
        self.quit = False
        self.move_right = 0
        self.move_left = 0
        self.move_up = 0
        self.move_down = 0
        self.letra = 1

    def update(self):
        """Manage user input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_left = 1
                if event.key == pygame.K_RIGHT:
                    self.move_right = 1
                if event.key == pygame.K_UP:
                    self.move_up = 1
                if event.key == pygame.K_DOWN:
                    self.move_down = 1
                if event.key == pygame.K_TAB:
                    self.letra += 1
            else:
                self.move_left = 0
                self.move_right = 0
                self.move_down = 0
                self.move_up = 0
                
