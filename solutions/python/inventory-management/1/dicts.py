"""Functions to keep track and alter inventory."""



def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.
 
    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    result_dict = {}
    for item in items:
        result_dict[item] = items.count(item)
    return result_dict


def add_items(inventory, items):
    for item in items:
        if item not in inventory.keys():
            inventory[item] = 1
            continue
        inventory[item] += 1
    return inventory
        
        
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    pass

def decrement_items(inventory, items):
    for item in items:
        i_item_value = inventory.get(item)
        if i_item_value and i_item_value > 0:
            inventory[item] -= 1
            if inventory[item] == 0:
                inventory[item]
    return inventory

def remove_item(inventory, item):
    if inventory.get(item):
        del inventory[item]
    return inventory

    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    pass


def list_inventory(inventory):
    return [(item, quantity) for item, quantity in inventory.items() if quantity > 0]
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    pass

