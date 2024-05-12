'''
Contains boat interaction screen, along with the victory screen when the
boat is rebuilt.
'''

import pygame
from classes.stats import player_inventory, player_stats
from classes.button import Button
from settings import MAP_SCREEN_RESOLUTION, BOAT_REQUIREMENTS

def open_boat_screen():
    screen = pygame.display.set_mode((500, 400))

    # Create fonts
    text_font = pygame.font.Font('./assets/SourceCodePro-Regular.ttf', 18)
    button_font = pygame.font.Font('./assets/SourceCodePro-Regular.ttf', 14)

    # Create buttons
    purchase_btn = Button('Repair', (200, 325, 100, 40), not can_build_boat())
    return_btn = Button('Return', (20, 20, 70, 30))

    # Main loop
    looping = True
    while looping:
        # Draw background
        screen.fill((0, 0, 0))

        # Print requirements
        WHITE = (255, 255, 255)
        screen.blit(text_font.render('Escape the island by repairing the boat.', True, WHITE), (30, 80))
        screen.blit(text_font.render('Resources required:', True, WHITE), (150, 140))
        screen.blit(button_font.render(f'{BOAT_REQUIREMENTS['wood']} Wood (you have {player_inventory.wood})', True, WHITE), (160, 170))
        screen.blit(button_font.render(f'{BOAT_REQUIREMENTS['copper']} Copper (you have {player_inventory.copper})', True, WHITE), (160, 190))
        screen.blit(button_font.render(f'{BOAT_REQUIREMENTS['iron']} Iron (you have {player_inventory.iron})', True, WHITE), (160, 210))

        # Draw buttons
        return_btn.render(screen, button_font)
        purchase_btn.render(screen, button_font)        

        # Event handling
        for event in pygame.event.get():
            # Window exit
            if event.type == pygame.QUIT:
                looping = False

            # Mouse pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if purchase_btn.is_pressed():
                    open_victory_screen()
                    looping = False
                    player_stats.won_game = True # Set this to true so that the game map automatically closes
                elif return_btn.is_pressed():
                    looping = False

        pygame.display.flip()

    # Reset resolution before returning to map screen
    pygame.display.set_mode(MAP_SCREEN_RESOLUTION)


def can_build_boat():
    '''
    Returns true if the player has enough resources to build the boat.
    '''

    return (player_inventory.wood >= BOAT_REQUIREMENTS['wood']
            and player_inventory.copper >= BOAT_REQUIREMENTS['copper']
            and player_inventory.iron >= BOAT_REQUIREMENTS['iron'])


def open_victory_screen():
    screen = pygame.display.set_mode((600, 600))

    # Create font
    text_font = pygame.font.Font('./assets/SourceCodePro-Regular.ttf', 34)

    # Load image
    thumbs_up = pygame.image.load('assets/thumbs-up.png')

    # Main loop
    looping = True
    while looping:
        # Background
        screen.fill((0, 0, 0))

        # Print victory message
        screen.blit(text_font.render('You Win!', True, (255, 255, 255)), (250, 50))

        # Show victory image
        screen.blit(thumbs_up, (60, 150))

        # TODO: Add image

        # Event handling
        for event in pygame.event.get():
            # Window exit
            if event.type == pygame.QUIT:
                looping = False

        pygame.display.flip()