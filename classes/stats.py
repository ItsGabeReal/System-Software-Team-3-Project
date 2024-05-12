'''
Code meant to track stats and inventory of different entities
'''

# Player statistics for actions such as fighting
class player_stats:
    player_health = 100
    player_hunger = 100
    tool_sword = 1
    tool_axe = 3
    tool_pickaxe = 1
    just_slept = False # Used to reset the map after the player sleeps

# Enemy statistics for fighting
class enemy_stats:
    enemy_health = 100

class player_inventory:
    gold = 0
    wood = 0
    copper = 0
    iron = 0
