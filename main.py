import pygame
from boat import open_boat_screen
from mining import get_mining_yield
from shop import open_shop_screen
from inn import open_inn_screen
from classes.world_map import world_map
from classes.stats import player_stats, player_inventory
from classes.message_board import Message_Board, show_message
import settings

# Constants
MOVE_DELAY = 150 # Delay between player movements when holding down an arrow key (in milliseconds)

# Pygame setup
pygame.init() # setup pygame
screen = pygame.display.set_mode(settings.MAP_SCREEN_RESOLUTION) # create a window
pygame.display.set_caption("Waterlogged") # set window name
map_font = pygame.font.Font('./assets/SourceCodePro-Regular.ttf', 24) # create a font that we can use to draw text
text_font = pygame.font.Font('./assets/SourceCodePro-Regular.ttf', 14)
pygame.key.set_repeat(MOVE_DELAY, MOVE_DELAY) # set repeat rate for keys. that way players can move by holding down the arrow keys

# Game setup
map = world_map()
mb = Message_Board()
show_message('Move with arrow keys. Interact with E.')

def loop():
    screen.fill((0, 0, 0)) # background

    map.render(screen, map_font, render_regeion=(65, 25)) # draw map on screen

    draw_game_info()

    mb.render(screen)

    pygame.display.flip() # render everything we've done


def draw_game_info():
    STAT_SPACING = 16 # vertical spacing between stat text
    PANEL_X = 10 # X offset
    PANEL_Y = 10 # Y offset

    # panel background
    pygame.draw.rect(screen, (150, 150, 150), (PANEL_X-1, PANEL_Y-1, 100+2, STAT_SPACING*7+2)) # thin grey border
    pygame.draw.rect(screen, (50, 50, 50), (PANEL_X, PANEL_Y, 100, STAT_SPACING*7))

    # player stats
    draw_text(text_font, 'Health: '+str(player_stats.player_health), (PANEL_X, PANEL_Y))
    draw_text(text_font, 'Hunger: '+str(player_stats.player_hunger), (PANEL_X, PANEL_Y+STAT_SPACING))
    
    # resources
    draw_text(text_font, 'Gold: '+str(player_inventory.gold), (PANEL_X, PANEL_Y+STAT_SPACING*3))
    draw_text(text_font, 'Wood: '+str(player_inventory.wood), (PANEL_X, PANEL_Y+STAT_SPACING*4))
    draw_text(text_font, 'Copper: '+str(player_inventory.copper), (PANEL_X, PANEL_Y+STAT_SPACING*5))
    draw_text(text_font, 'Iron: '+str(player_inventory.iron), (PANEL_X, PANEL_Y+STAT_SPACING*6))
    

def on_key_pressed(event: pygame.event.Event):
    # Player movement
    if event.key == pygame.K_UP:
        map.move_player('n')
    elif event.key == pygame.K_DOWN:
        map.move_player('s')
    elif event.key == pygame.K_RIGHT:
        map.move_player('e')
    elif event.key == pygame.K_LEFT:
        map.move_player('w')

    # Object interaction
    elif event.key == pygame.K_e:
        letter = map.get_nearby_interactable() # look for a nearby object to interact with

        if letter == '': # nothing interactable nearby, so do nothing
            return
        
        elif letter == 'B': # blacksmith
            print('interacted with Blacksmith')
        
        elif letter == 'H': # inn
            open_inn_screen()
            if player_stats.just_slept:
                player_stats.just_slept = False
                map.initialize() # Reset map resources


        elif letter == 'S': # shop
            open_shop_screen()
        
        elif letter == 'U': # boat
            open_boat_screen()
        
        elif letter == 'O' or letter == 'T': # resource
            resource = map.get_nearby_resource() # get resource attributes (health and type)
            
            if letter == 'O':
                resource.mine(10 * player_stats.tool_pickaxe)
            else:
                resource.mine(10 * player_stats.tool_axe)

            if resource.is_mined():
                if resource.type == 'wood':
                    amount = get_mining_yield(player_stats.tool_axe)
                    player_inventory.wood += amount
                    show_message(f'Harvested {amount} Wood')
                elif resource.type == 'copper':
                    amount = get_mining_yield(player_stats.tool_pickaxe)
                    player_inventory.copper += amount                    
                    show_message(f'Mined {amount} Copper')
                else:
                    amount = get_mining_yield(player_stats.tool_pickaxe)
                    player_inventory.iron += amount
                    show_message(f'Mined {amount} Iron')

                map.remove_resource(resource.location)
            else:
                show_message(f'Mining resource. {resource.health}% Remaining.')

def on_mouse_pressed(event: pygame.event.Event):
    # example mouse interaction code
    if event.button == 1: # Left mouse button
        print("left mouse button pressed")


def draw_text(font: pygame.font.Font, message, position: tuple[int, int], color = (255, 255, 255)):
    img = font.render(message, True, color)
    screen.blit(img, position)


if __name__ == '__main__':
    # Run gameplay loop until the game window is closed
    exit = False
    while exit == False and not player_stats.won_game:
        loop()

        # Handle input events (like key presses or mouse presses)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                on_key_pressed(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                on_mouse_pressed(event)
            elif event.type == pygame.QUIT:
                pygame.quit()
                exit = True
