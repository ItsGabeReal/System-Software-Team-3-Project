import pygame
from classes.world_map import world_map
from classes.stats import player_stats, player_inventory

# Constants
MOVE_DELAY = 200 # Delay between player movements when holding down an arrow key (in milliseconds)

# Pygame setup
pygame.init() # setup pygame
screen = pygame.display.set_mode((960, 680)) # create a window
pygame.display.set_caption("Waterlogged") # set window name
map_font = pygame.font.Font('./assets/SourceCodePro-Regular.ttf', 24) # create a font that we can use to draw text
text_font = pygame.font.Font('./assets/SourceCodePro-Regular.ttf', 14)
pygame.key.set_repeat(MOVE_DELAY, MOVE_DELAY) # set repeat rate for keys. that way players can move by holding down the arrow keys

# Game setup
map = world_map()


def loop():
    screen.fill((0, 0, 0)) # background

    map.render(screen, map_font, render_regeion=(61, 21)) # draw map on screen

    draw_game_info()

    pygame.display.flip() # render everything we've done

def draw_game_info():
    # Print gameplay information
    STAT_SPACING = 16
    
    # draw rect background
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 100, STAT_SPACING*7))

    # player stats
    draw_text(text_font, 'Health: '+str(player_stats.player_health), (0, 0))
    draw_text(text_font, 'Hunger: '+str(player_stats.player_hunger), (0, STAT_SPACING))
    draw_text(text_font, 'Gold: '+str(player_inventory.gold), (0, STAT_SPACING*3))
    draw_text(text_font, 'Wood: '+str(player_inventory.wood), (0, STAT_SPACING*4))
    draw_text(text_font, 'Copper: '+str(player_inventory.copper), (0, STAT_SPACING*5))
    draw_text(text_font, 'Iron: '+str(player_inventory.iron), (0, STAT_SPACING*6))
    
    # resources
    
    # tool levels


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
            print('interacted with Inn')
        
        elif letter == 'S': # shop
            print('interacted with Shop')
        
        elif letter == 'U': # boat
            print('interacted with Boat')
        
        elif letter == 'O' or letter == 'T': # resource
            resource = map.get_nearby_resource() # get resource attributes (health and type)
            
            # TODO: Alter mining rate acording to tool level
            resource.mine(20) # partially mine the resource

            if resource.is_mined():
                if resource.type == 'wood':
                    player_inventory.wood += 1
                elif resource.type == 'copper':
                    player_inventory.copper += 1
                else:
                    player_inventory.iron += 1
                
                map.remove_resource(resource.location)
            else:
                print('Mined resource.', resource.health, 'health remaining')
            

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
    while exit == False:
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
