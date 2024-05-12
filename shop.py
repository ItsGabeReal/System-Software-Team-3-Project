'''
shop.py
Defines the Shop class for managing item transactions in the game
'''

import pygame
from classes.stats import player_inventory, player_stats
from classes.button import Button
from settings import SHOP_INVENTORY, MAP_SCREEN_RESOLUTION

LIST_POSITION = (20, 150)
BUTTON_SIZE = (70, 30)
BUTTON_X_OFFSET = 150
SELL_LIST_X = 250
ITEM_SPACING = 50

def open_shop_screen():
    screen = pygame.display.set_mode((500, 530))

    # Create font
    text_font = pygame.font.Font('./assets/SourceCodePro-Regular.ttf', 14)
    button_font = pygame.font.Font('./assets/SourceCodePro-Regular.ttf', 12)

    # Create buttons
    close_btn = Button('Leave', (20, 20, 50, 20))
    axe_btn = Button('-'+str(SHOP_INVENTORY['Axe']['price'])+' Gold', (LIST_POSITION[0]+BUTTON_X_OFFSET, LIST_POSITION[1], BUTTON_SIZE[0], BUTTON_SIZE[1]))
    pickaxe_btn = Button('-'+str(SHOP_INVENTORY['Pickaxe']['price'])+' Gold', (LIST_POSITION[0]+BUTTON_X_OFFSET, LIST_POSITION[1]+ITEM_SPACING, BUTTON_SIZE[0], BUTTON_SIZE[1]))
    sword_btn = Button('-'+str(SHOP_INVENTORY['Sword']['price'])+' Gold', (LIST_POSITION[0]+BUTTON_X_OFFSET, LIST_POSITION[1]+ITEM_SPACING*2, BUTTON_SIZE[0], BUTTON_SIZE[1]))
    apple_btn = Button('-'+str(SHOP_INVENTORY['Apple']['price'])+' Gold', (LIST_POSITION[0]+BUTTON_X_OFFSET, LIST_POSITION[1]+ITEM_SPACING*3, BUTTON_SIZE[0], BUTTON_SIZE[1]))
    corn_btn = Button('-'+str(SHOP_INVENTORY['Corn']['price'])+' Gold', (LIST_POSITION[0]+BUTTON_X_OFFSET, LIST_POSITION[1]+ITEM_SPACING*4, BUTTON_SIZE[0], BUTTON_SIZE[1]))
    wood_btn = Button('-'+str(SHOP_INVENTORY['Wood']['price'])+' Gold', (LIST_POSITION[0]+BUTTON_X_OFFSET, LIST_POSITION[1]+ITEM_SPACING*5, BUTTON_SIZE[0], BUTTON_SIZE[1]))
    copper_btn = Button('-'+str(SHOP_INVENTORY['Copper']['price'])+' Gold', (LIST_POSITION[0]+BUTTON_X_OFFSET, LIST_POSITION[1]+ITEM_SPACING*6, BUTTON_SIZE[0], BUTTON_SIZE[1]))
    iron_btn = Button('-'+str(SHOP_INVENTORY['Iron']['price'])+' Gold', (LIST_POSITION[0]+BUTTON_X_OFFSET, LIST_POSITION[1]+ITEM_SPACING*7, BUTTON_SIZE[0], BUTTON_SIZE[1]))
    sell_wood_btn = Button('+'+str(SHOP_INVENTORY['Wood']['price'])+' Gold', (SELL_LIST_X+BUTTON_X_OFFSET, LIST_POSITION[1], BUTTON_SIZE[0], BUTTON_SIZE[1]))
    sell_copper_btn = Button('+'+str(SHOP_INVENTORY['Copper']['price'])+' Gold', (SELL_LIST_X+BUTTON_X_OFFSET, LIST_POSITION[1]+ITEM_SPACING, BUTTON_SIZE[0], BUTTON_SIZE[1]))
    sell_iron_btn = Button('+'+str(SHOP_INVENTORY['Iron']['price'])+' Gold', (SELL_LIST_X+BUTTON_X_OFFSET, LIST_POSITION[1]+ITEM_SPACING*2, BUTTON_SIZE[0], BUTTON_SIZE[1]))

    # Main loop
    looping = True
    while looping:
        # Background
        screen.fill((0, 0, 0))

        # Shop title
        screen.blit(text_font.render('Shop', True, (255, 255, 255)), (225, 20))

        # Leave button
        close_btn.render(screen, button_font)

        # Show current stats
        screen.blit(text_font.render('Current stats:', True, (255, 255, 255)), (50, 50))
        screen.blit(button_font.render(f'{player_inventory.gold} Gold | {player_inventory.wood} Wood | {player_inventory.copper} Copper | {player_inventory.iron} Iron', True, (255, 255, 255)), (50, 70))
        screen.blit(button_font.render(f'Axe: Level {player_stats.tool_axe} | Pickaxe: Level {player_stats.tool_pickaxe} | Sword: Level {player_stats.tool_sword}', True, (255, 255, 255)), (50, 90))
        screen.blit(button_font.render(f'{player_stats.player_hunger} Hunger', True, (255, 255, 255)), (50, 110))

        # Display options
        screen.blit(text_font.render('Upgrade Axe:', True, (255, 255, 255)), (LIST_POSITION[0], LIST_POSITION[1]))
        axe_btn.render(screen, button_font)
        screen.blit(text_font.render('Upgrade Pickaxe:', True, (255, 255, 255)), (LIST_POSITION[0], LIST_POSITION[1]+ITEM_SPACING))
        pickaxe_btn.render(screen, button_font)
        screen.blit(text_font.render('Upgrade Sword:', True, (255, 255, 255)), (LIST_POSITION[0], LIST_POSITION[1]+ITEM_SPACING*2))
        sword_btn.render(screen, button_font)
        screen.blit(text_font.render('Buy Apple:', True, (255, 255, 255)), (LIST_POSITION[0], LIST_POSITION[1]+ITEM_SPACING*3))
        apple_btn.render(screen, button_font)
        screen.blit(text_font.render('Buy Corn:', True, (255, 255, 255)), (LIST_POSITION[0], LIST_POSITION[1]+ITEM_SPACING*4))
        corn_btn.render(screen, button_font)
        screen.blit(text_font.render('Buy Wood:', True, (255, 255, 255)), (LIST_POSITION[0], LIST_POSITION[1]+ITEM_SPACING*5))
        wood_btn.render(screen, button_font)
        screen.blit(text_font.render('Buy Copper:', True, (255, 255, 255)), (LIST_POSITION[0], LIST_POSITION[1]+ITEM_SPACING*6))
        copper_btn.render(screen, button_font)
        screen.blit(text_font.render('Buy Iron:', True, (255, 255, 255)), (LIST_POSITION[0], LIST_POSITION[1]+ITEM_SPACING*7))
        iron_btn.render(screen, button_font)
        # Sell buttons
        screen.blit(text_font.render('Sell Wood:', True, (255, 255, 255)), (SELL_LIST_X, LIST_POSITION[1]))
        sell_wood_btn.render(screen, button_font)
        screen.blit(text_font.render('Sell Copper:', True, (255, 255, 255)), (SELL_LIST_X, LIST_POSITION[1]+ITEM_SPACING))
        sell_copper_btn.render(screen, button_font)
        screen.blit(text_font.render('Sell Iron:', True, (255, 255, 255)), (SELL_LIST_X, LIST_POSITION[1]+ITEM_SPACING*2))
        sell_iron_btn.render(screen, button_font)

        # Event handling
        for event in pygame.event.get():
            # Window exit
            if event.type == pygame.QUIT:
                looping = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                item_type = None
                selling = False

                if close_btn.is_pressed():
                    looping = False
                elif axe_btn.is_pressed() and player_stats.tool_axe < 3:
                    item_type = 'Axe'
                elif pickaxe_btn.is_pressed() and player_stats.tool_pickaxe < 3:
                    item_type = 'Pickaxe'
                elif sword_btn.is_pressed() and player_stats.tool_sword < 3:
                    item_type = 'Sword'
                elif apple_btn.is_pressed():
                    item_type = 'Apple'
                elif corn_btn.is_pressed():
                    item_type = 'Corn'
                elif wood_btn.is_pressed():
                    item_type = 'Wood'
                elif copper_btn.is_pressed():
                    item_type = 'Copper'
                elif iron_btn.is_pressed():
                    item_type = 'Iron'
                elif sell_wood_btn.is_pressed():
                    selling = True
                    item_type = 'Wood'
                elif sell_copper_btn.is_pressed():
                    selling = True
                    item_type = 'Copper'
                elif sell_iron_btn.is_pressed():
                    selling = True
                    item_type = 'Iron'

                if item_type == None:
                    print('Error purchasing item')
                    continue            
                
                if selling:
                    sell_item(item_type)
                else:
                    buy_item(item_type)

        pygame.display.flip()

    # Reset resolution before returning to map screen
    pygame.display.set_mode(MAP_SCREEN_RESOLUTION)

def buy_item(item_name):
    if item_name in SHOP_INVENTORY and player_inventory.gold >= SHOP_INVENTORY[item_name]['price']:
        # Withdraw gold
        player_inventory.gold -= SHOP_INVENTORY[item_name]['price']
        
        # Apply purchase
        if item_name == 'Axe':
            player_stats.tool_axe = min(player_stats.tool_axe+1, 3)
        elif item_name == 'Sword':
            player_stats.tool_sword = min(player_stats.tool_sword+1, 3)
        elif item_name == 'Pickaxe':
            player_stats.tool_pickaxe = min(player_stats.tool_pickaxe+1, 3)
        elif item_name == 'Apple':
            player_stats.player_hunger = min(player_stats.player_hunger+35, 100)
        elif item_name == 'Corn':
            player_stats.player_hunger = min(player_stats.player_hunger+25, 100)
        elif item_name == 'Iron':
            player_inventory.iron += 1
        elif item_name == 'Copper':
            player_inventory.copper += 1
        elif item_name == 'Wood':
            player_inventory.wood += 1
        print(f'You bought {item_name} for {SHOP_INVENTORY[item_name]["price"]} gold.')
    else:
        print('You cannot afford that item.')

def sell_item(item_name):
    # Give the player gold
    player_inventory.gold += SHOP_INVENTORY[item_name]['price']
    
    if item_name == 'Iron' and player_inventory.iron > 0:
        player_inventory.iron -= 1
    elif item_name == 'Copper' and player_inventory.copper > 0:
        player_inventory.copper -= 1
    elif item_name == 'Wood' and player_inventory.wood > 0:
        player_inventory.wood -= 1
    else:
        print('You cannot sell an item you don\'t have')
