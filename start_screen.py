import pygame
from settings import MAP_SCREEN_RESOLUTION
from classes.button import Button

def open_start_screen():
    start_screen = pygame.display.set_mode((400, 250))

    # Create font
    text_font = pygame.font.Font('./assets/SourceCodePro-Regular.ttf', 14)
    button_font = pygame.font.Font('./assets/SourceCodePro-Regular.ttf', 12)

    # Create buttons
    start_btn = Button('Start', (160, 175, 80, 40))

    # Main loop
    looping = True
    while looping:
        # Background
        start_screen.fill((0, 0, 0))

        # Introduction text
        start_screen.blit(text_font.render('Welcome to Waterlogged!', True, (255, 255, 255)), (110, 20))
        start_screen.blit(text_font.render('You were sailing the open seas, when suddenly', True, (255, 255, 255)), (10, 50))
        start_screen.blit(text_font.render('your ship crashed into a small island.', True, (255, 255, 255)), (10, 70))
        start_screen.blit(text_font.render('You must scavenge this island for enough', True, (255, 255, 255)), (10, 100))
        start_screen.blit(text_font.render('resources to repair the ship and return to sea.', True, (255, 255, 255)), (10, 120))

        # Start button
        start_btn.render(start_screen, button_font)

        # Event handling
        for event in pygame.event.get():
            # Window exit
            if event.type == pygame.QUIT:
                looping = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn.is_pressed():
                    looping = False

        pygame.display.flip()

    # Reset resolution before returning to map screen
    pygame.display.set_mode(MAP_SCREEN_RESOLUTION)