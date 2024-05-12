import random

def get_mining_yield(tool_level):
    '''
    Returns the number of resources gained by mining an ore or a tree
    based on the level of their respective tools.
    '''

    if tool_level == 1:
        resource_yield = 2
    elif tool_level == 2:
        resource_yield = random.randint(3, 7)
    else:
        resource_yield = random.randint(10, 15)

    return resource_yield
