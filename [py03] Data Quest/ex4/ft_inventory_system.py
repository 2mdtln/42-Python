# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_inventory_system.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/04 17:54:08 by mtaheri            #+#    #+#             #
#   Updated: 2026/03/06 17:54:23 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import sys


class Item:
    def __init__(self, name: str, type: str,
                 quantity: int, value: float) -> None:
        self.__name = name
        self.__type = type
        self.__quantity = quantity
        self.__value = value

    def get_val(self, get: str) -> any:
        return {
            "name": self.__name,
            "type": self.__type,
            "quantity": self.__quantity,
            "value": self.__value
        }.get(get, "???")

    @classmethod
    def get_type(_, name: str) -> str:
        if name == "potion":
            return "Moderate"
        elif name in ("sword", "shield", "armor", "helmet"):
            return "Scarce"
        else:
            return "other"


class Inventory:
    def __init__(self) -> None:
        self.__items = dict()

    def add_item(self, item: Item) -> None:
        name = item.get_val("name")
        if name in self.__items:
            self.__items[name]["quantity"] += item.get_val("quantity")
        else:
            self.__items[name] = {
                "type": item.get_val("type"),
                "quantity": item.get_val("quantity"),
                "value": item.get_val("value")
            }

    def get_items(self) -> dict:
        return self.__items


class Player:
    def __init__(self) -> None:
        self.__inventory = Inventory()

    def get_inventory(self) -> dict:
        return self.__inventory.get_items()

    def pickup(self, item: Item) -> None:
        self.__inventory.add_item(item)


def parse(player: Player):
    for arg in sys.argv[1:]:
        parts = arg.split(":")
        if len(parts) == 2:
            player.pickup(Item(parts[0], Item.get_type(parts[0]),
                               int(parts[1]), int(parts[1]) * 8.3))


def total_items(player_inventory):
    total_items = 0
    for item_name, item_data in player_inventory.items():
        total_items += item_data['quantity']
    return total_items


def get_category_items(category: str, player_inventory):
    category_items = dict()
    for item in player_inventory.keys():
        if player_inventory[item]["type"] == category:
            category_items.update({item: player_inventory[item]["quantity"]})
    return category_items


def get_categories(player_inventory) -> list:
    categories = dict()
    for item in player_inventory:
        item_type = player_inventory[item]["type"]
        categories[item_type] = None
    return list(categories.keys())


def get_stats(player_inventory):
    most_item = None
    most_qty = 0
    least_item = None
    least_qty = None
    for item in player_inventory:
        qty = player_inventory.get(item).get("quantity")
        if qty > most_qty:
            most_item = item
            most_qty = qty
        if least_qty is None or qty < least_qty:
            least_item = item
            least_qty = qty
    return most_item, most_qty, least_item, least_qty


def get_restock_needed(player_inventory, restock_threshold=1):
    restock_list = []
    for item in player_inventory:
        qty = player_inventory.get(item).get("quantity")
        if qty <= restock_threshold:
            restock_list = restock_list + [item]
    return restock_list


def main(player_inventory):
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items(player_inventory)}")
    print(f"Unique item types: {len(player_inventory)}")

    print("\n=== Current Inventory ===")
    for item in player_inventory.keys():
        print(f"{item}: {player_inventory.get(item).get("quantity")} "
              f"unit ({player_inventory.get(item).get("value"):.2f}%)")

    print("\n=== Inventory Statistics ===")
    most_item, most_qty, least_item, least_qty = get_stats(player_inventory)
    print(f"Most abundant: {most_item} ({most_qty} units)")
    print(f"Least abundant: {least_item} ({least_qty} unit)")

    print("\n=== Item Categories ===")
    for category in get_categories(player_inventory):
        print(f"{category}: {get_category_items(category, player_inventory)}")

    print("\n=== Management Suggestions ===")
    result = "Restock needed: "
    for item in get_restock_needed(player_inventory):
        result = result + item + ", "
    print(result[:-2])

    print("\n=== Dictionary Properties Demo ===")
    keys_str = ""
    for key in player_inventory.keys():
        keys_str = keys_str + key + ", "
    keys_str = keys_str[:-2]
    print(f"Dictionary keys: {keys_str}")

    values_str = ""
    for item in player_inventory:
        qty = player_inventory[item].get("quantity")
        values_str = values_str + str(qty) + ", "
    values_str = values_str[:-2]
    print(f"Dictionary values: {values_str}")

    print(f"Sample lookup - 'sword' in inventory: "
          f"{"sword" in player_inventory}")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print("Usage: python3 ft_inventory_system.py item:quantity ...")
    else:
        player = Player()
        parse(player)
        player_inventory = player.get_inventory()
        main(player_inventory)
