'''
Contains the button class, which simplifies the creation, rendering,
and interaction handling of a button.
'''

import pygame

class Button:
    def __init__(self, text: str, dimensions: tuple[int, int, int, int], starts_disabled = False) -> None:
        self.__text = text
        self.__dimensions = dimensions
        self.__disabled = starts_disabled


    def render(self, screen: pygame.Surface, font: pygame.font.Font):
        # Determine color
        if self.__disabled:
            color = (100, 100, 100)
        elif self.hovering_button():
            color = (220, 220, 220)
        else:
            color = (200, 200, 200)

        # Draw button background
        pygame.draw.rect(screen, color, self.__dimensions)

        img = font.render(self.__text, True, (0, 0, 0))
        text_x = self.__dimensions[0] + self.__dimensions[2]//2 - img.get_rect()[2]//2
        text_y = self.__dimensions[1] + self.__dimensions[3]//2 - img.get_rect()[3]//2
        screen.blit(img, (text_x, text_y))


    def set_enabled(self, enabled: bool):
        '''
        Enables/disables the button, which changes the button's visuals,
        and does not respond to presses.
        '''

        self.__disabled = not enabled
    

    def hovering_button(self) -> bool:
        '''
        Returns true if the mouse is hovering over the button.
        '''

        mouse_pos = pygame.mouse.get_pos()

        return (mouse_pos[0] >= self.__dimensions[0]
            and mouse_pos[0] <= self.__dimensions[0]+self.__dimensions[2]
            and mouse_pos[1] >= self.__dimensions[1]
            and mouse_pos[1] <= self.__dimensions[1]+self.__dimensions[3])


    def is_pressed(self) -> bool:
        '''
        Returns true if the mouse is pressed while on top of the button.
        '''
        
        if self.__disabled:
            return False
        
        return pygame.mouse.get_pressed()[0] and self.hovering_button()
