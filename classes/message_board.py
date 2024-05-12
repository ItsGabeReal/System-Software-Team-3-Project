import pygame
import time
import os
from settings import MAP_SCREEN_RESOLUTION

MESSAGE_DURATION = 5 # Duration messages will be shown in seconds

class Message_Board:
    current_message: str = 'Test message. POGGIES!'
    message_start_time = 0

    def __init__(self) -> None:
        font_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'SourceCodePro-Regular.ttf')
        self.font = pygame.font.Font(font_path, 16)

    def render(self, screen: pygame.Surface):
        if not self.__should_show_message():
            return
        
        # Render text
        text_img = self.font.render(self.current_message, True, (255, 255, 255))

        # Determine dimensions
        BOX_PADDING = 15
        Y_POSITION = 30
        text_size = text_img.get_size()
        box_x = MAP_SCREEN_RESOLUTION[0]//2 - text_size[0]//2 - BOX_PADDING
        box_y = Y_POSITION
        box_w = text_size[0] + BOX_PADDING*2
        box_h = text_size[1] + BOX_PADDING*2

        # Draw background box
        pygame.draw.rect(screen, (150, 150, 150), (box_x-1, box_y-1, box_w+2, box_h+2)) # thin grey border
        pygame.draw.rect(screen, (50, 50, 50), (box_x, box_y, box_w, box_h))

        # Draw text
        screen.blit(text_img, (MAP_SCREEN_RESOLUTION[0]//2 - text_size[0]//2, Y_POSITION+BOX_PADDING))

    def __should_show_message(self) -> bool:
        return time.time() - self.message_start_time < MESSAGE_DURATION

def show_message(message: str):
    Message_Board.current_message = message
    Message_Board.message_start_time = time.time()