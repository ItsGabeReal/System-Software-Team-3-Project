import pygame
from classes.stats import player_inventory, player_stats
from classes.button import Button
from classes.message_board import show_message
from settings import SHOP_INVENTORY, MAP_SCREEN_RESOLUTION, SLEEP_COST

def open_inn_screen():
    screen = pygame.display.set_mode((300, 300))

    # Create font
    text_font = pygame.font.Font('./assets/SourceCodePro-Regular.ttf', 14)
    button_font = pygame.font.Font('./assets/SourceCodePro-Regular.ttf', 12)
    tutorial_font = pygame.font.Font('./assets/SourceCodePro-Regular.ttf', 10)

    # Create buttons
    close_btn = Button('Leave', (20, 20, 50, 20))
    sleep_btn = Button('Sleep (-'+str(SLEEP_COST)+' Gold)', (90, 175, 120, 50))

    # Main loop
    looping = True
    while looping:
        # Background
        screen.fill((0, 0, 0))

        # Shop title
        screen.blit(text_font.render('Inn', True, (255, 255, 255)), (130, 20))

        # Leave button
        close_btn.render(screen, button_font)

        # Player stats
        screen.blit(text_font.render(f'{player_stats.player_health} Health | {player_inventory.gold} Gold', True, (255, 255, 255)), (50, 70))

        # Sleep button
        sleep_btn.render(screen, button_font)
        
        # Tutorial text
        screen.blit(tutorial_font.render('Sleeping refills your health.', True, (255, 255, 255)), (20, 250))
        screen.blit(tutorial_font.render('It also resets all the resources on the map.', True, (255, 255, 255)), (20, 270))

        # Event handling
        for event in pygame.event.get():
            # Window exit
            if event.type == pygame.QUIT:
                looping = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if close_btn.is_pressed():
                    looping = False
                elif sleep_btn.is_pressed():
                    if player_inventory.gold >= SLEEP_COST:
                        player_inventory.gold -= SLEEP_COST
                        player_stats.just_slept = True
                        player_stats.player_health = 100
                        show_message('You slept. Resources have been reset.')
                        looping = False
                    else:
                        print('You cannot afford to sleep. Sorry.')

        pygame.display.flip()

    # Reset resolution before returning to map screen
    pygame.display.set_mode(MAP_SCREEN_RESOLUTION)
