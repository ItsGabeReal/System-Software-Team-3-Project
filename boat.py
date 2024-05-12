'''
Contains boat interaction screen, along with the victory screen when the
boat is rebuilt.
'''

import pygame
from classes.stats import player_inventory
from classes.button import Button
from settings import MAP_SCREEN_RESOLUTION, BOAT_REQUIREMENTS

def open_boat_screen():
    pygame.display.set_caption("Broken Boat")
    screen = pygame.display.set_mode((500, 500))

    # Create fonts
    text_font = pygame.font.Font('./assets/SourceCodePro-Regular.ttf', 18)
    button_font = pygame.font.Font('./assets/SourceCodePro-Regular.ttf', 14)

    # Create buttons
    purchase_btn = Button('Purchase', (200, 400, 100, 40), not can_build_boat())
    return_btn = Button('Return', (20, 20, 70, 30))

    # Main loop
    looping = True
    while looping:
        # Draw background
        screen.fill((0, 0, 0))

        # Print requirements
        WHITE = (255, 255, 255)        
        screen.blit(text_font.render('Escape the island by building the boat.', True, WHITE), (100, 100))
        screen.blit(text_font.render('Resources required:', True, WHITE), (100, 120))
        screen.blit(text_font.render('Wood: '+str(player_inventory.wood)+'/'+str(BOAT_REQUIREMENTS['wood']), True, WHITE), (100, 140))
        screen.blit(text_font.render('Copper: '+str(player_inventory.copper)+'/'+str(BOAT_REQUIREMENTS['copper']), True, WHITE), (100, 160))
        screen.blit(text_font.render('Iron: '+str(player_inventory.iron)+'/'+str(BOAT_REQUIREMENTS['iron']), True, WHITE), (100, 180))

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
    pygame.display.set_caption("You Win!")
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
