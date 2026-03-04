# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_inventory_system.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/04 17:54:08 by mtaheri            #+#    #+#             #
#   Updated: 2026/03/04 23:14:28 by mtaheri           ###   ########.fr       #
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
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        for arg in sys.argv[1:]:
            parts = arg.split(":")
            if len(parts) == 2:
                player.pickup(Item(parts[0], Item.get_type(parts[0]),
                                   int(parts[1]), int(parts[1]) * 8.3))


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    player = Player()
    parse(player)
    print("\n=== Current Inventory ===")
    print(f"{player.get_inventory()}:")
