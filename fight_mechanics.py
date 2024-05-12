import pygame
import random
from classes.stats import player_stats, enemy_stats, player_inventory
from classes.button import Button
from classes.message_board import show_message
from settings import MAP_SCREEN_RESOLUTION

# Constants
FONT_SIZE_HEALTH = 16
FONT_SIZE_CHARS = 36
HEALTH_BAR_COLOR = (255, 100, 100)

'''
Section of code determines outcome of actions during a fight event
'''
# Determines damage output of sword based on hunger and tool level
def fighting_action():
    tool_sword = player_stats.tool_sword
    player_hunger = player_stats.player_hunger

    if tool_sword == 1:
        flat_damage = random.randint(5, 10)
    elif tool_sword == 2:
        flat_damage = random.randint(10, 15)
    else:
        flat_damage = random.randint(20, 30)

    if player_hunger >= 75:
        efficacy = 1.0
    elif player_hunger >= 50:
        efficacy = 0.75
    elif player_hunger >= 25:
        efficacy = 0.50
    else:
        efficacy = 0.25

    attack_damage_result = flat_damage * efficacy

    return round(attack_damage_result)
#Determines damage dealt to player by enemy after a fight action event was initated
def enemy_attack():
    enemy_damage = random.randint(1, 3)
    return enemy_damage
#Determines if players flee attempt in fight is successful
def runaway_calc():
    runaway_chance = random.randint(1, 25)
    if player_stats.player_hunger >= runaway_chance:
        return True
    else:
        return False

'''
Section of code initializes and sets up fight event when triggered by chance in the world_map file
'''
def fight_encounter():
    # Pygame setup
    screen = pygame.display.set_mode((500, 500))

    # Pygame font setup
    font_health = pygame.font.Font(None, FONT_SIZE_HEALTH)
    font_chars = pygame.font.Font(None, FONT_SIZE_CHARS)
    font_tutorial = pygame.font.Font('./assets/SourceCodePro-Regular.ttf', 10)

    # Text surfaces
    player_text = font_chars.render("P", True, (255, 255, 255))

    # Enemy image
    enemy_img = pygame.image.load('assets/meanie.png')

    # Health and hunger bars
    player_health_bar = font_health.render(f"Health: {player_stats.player_health}", True, HEALTH_BAR_COLOR)
    enemy_health_bar = font_health.render(f"Health: {enemy_stats.enemy_health}", True, HEALTH_BAR_COLOR)
    player_hunger_bar = font_health.render(f"Hunger: {player_stats.player_hunger}", True, HEALTH_BAR_COLOR)

    # Calculate text sizes
    player_text_size = player_text.get_size()

    # Calculate health and hunger bar positions
    player_health_bar_pos = (100 - player_health_bar.get_width() / 2, 100 + player_text_size[1])
    player_hunger_bar_pos = (
    100 - player_hunger_bar.get_width() / 2, player_health_bar_pos[1] + player_health_bar.get_height() + 5)
    enemy_health_bar_pos = (350, 75)

    # Set up buttons
    button_width = FONT_SIZE_CHARS * 4  # Adjust button width as needed
    button_height = FONT_SIZE_CHARS + 10  # Adjust button height as needed
    fight_button_location = ((250 - button_width) / 2, 375)
    run_button_location = ((250 - button_width) / 2 + 250, 375)
    fight_btn = Button('Fight', (fight_button_location[0], fight_button_location[1], button_width, button_height))
    run_btn = Button('Run', (run_button_location[0], run_button_location[1], button_width, button_height))

    # Main loop
    running_fight = True
    while running_fight:
        screen.fill((0, 0, 0))

        # Draw player text
        screen.blit(player_text, (100, 100))
        screen.blit(player_health_bar, player_health_bar_pos)
        screen.blit(player_hunger_bar, player_hunger_bar_pos)

        # Draw enemy image and health
        screen.blit(enemy_img, (300, 100))
        screen.blit(enemy_health_bar, enemy_health_bar_pos)

        # Draw buttons
        fight_btn.render(screen, font_chars)
        run_btn.render(screen, font_chars)

        # Draw tutorial text
        screen.blit(font_tutorial.render('Winning gains you resources, and losing looses you resources.', True, (255, 255, 255)), (20, 460))
        screen.blit(font_tutorial.render('Your attacks are less effective if you are hungry.', True, (255, 255, 255)), (20, 480))
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flee_attempt = runaway_calc()
                if flee_attempt == True:
                    running_fight = False
                    enemy_stats.enemy_health = 100
                    show_message('You fled the fight')
                else:
                    damage_recieved = enemy_attack()
                    player_stats.player_health -= damage_recieved
                    if player_stats.player_health <= 0:
                        running_fight = False
                        player_stats.player_health = 100
                        enemy_stats.enemy_health = 100
                        current_copper = player_inventory.copper
                        player_inventory.copper = max(player_inventory.copper-10, 0)
                        show_message(f'Fight lost. Enemy took {current_copper-player_inventory.copper} copper')
                # Update player and enemy health display
                player_health_bar = font_health.render(f"Health: {player_stats.player_health}", True, HEALTH_BAR_COLOR)
                enemy_health_bar = font_health.render(f"Health: {enemy_stats.enemy_health}", True, HEALTH_BAR_COLOR)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if fight_btn.is_pressed():
                    # Handles health/hunger tracking and damage exchange on fight button event click
                    damage_dealt = fighting_action()
                    enemy_stats.enemy_health -= damage_dealt
                    damage_recieved = enemy_attack()
                    player_stats.player_hunger = max(player_stats.player_hunger-3, 0)
                    player_stats.player_health = max(player_stats.player_health-damage_recieved, 0)
                    #Ends fight event if player health or enemy health is fully depleted
                    fight_over = False
                    if enemy_stats.enemy_health <= 0:
                        running_fight = False
                        enemy_stats.enemy_health = 100
                        player_inventory.copper += 4
                        show_message(f'Fight won. You gained 4 copper')
                    elif player_stats.player_health <= 0:
                        running_fight = False
                        player_stats.player_health = 100
                        enemy_stats.enemy_health = 100
                        current_copper = player_inventory.copper
                        player_inventory.copper = max(player_inventory.copper-10, 0)
                        show_message(f'Fight lost. Enemy took {current_copper-player_inventory.copper} copper')

                    # Update player and enemy health display
                    player_health_bar = font_health.render(f"Health: {player_stats.player_health}", True, HEALTH_BAR_COLOR)
                    enemy_health_bar = font_health.render(f"Health: {enemy_stats.enemy_health}", True, HEALTH_BAR_COLOR)
                    player_hunger_bar = font_health.render(f"Hunger: {player_stats.player_hunger}", True, HEALTH_BAR_COLOR)

                elif run_btn.is_pressed():
                    flee_attempt = runaway_calc()
                    if flee_attempt == True:
                        running_fight = False
                        enemy_stats.enemy_health = 100
                        show_message('You fled the fight')
                    else:
                        damage_recieved = enemy_attack()
                        player_stats.player_health -= damage_recieved
                        if player_stats.player_health <= 0:
                            running_fight = False
                            player_stats.player_health = 100
                            enemy_stats.enemy_health = 100

                    # Update player and enemy health display
                    player_health_bar = font_health.render(f"Health: {player_stats.player_health}", True, HEALTH_BAR_COLOR)
                    enemy_health_bar = font_health.render(f"Health: {enemy_stats.enemy_health}", True, HEALTH_BAR_COLOR)



        pygame.display.flip()

    # Reset resolution before returning to map screen
    pygame.display.set_mode(MAP_SCREEN_RESOLUTION)
