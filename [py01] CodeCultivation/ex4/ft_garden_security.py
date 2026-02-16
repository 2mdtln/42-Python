#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_security.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/16 13:05:07 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/16 23:24:56 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = 0
        self.age = 0
        print(f"Plant created: {self.get_name()}")
        self.set_height(height)
        self.set_age(age)

    def get_info(self) -> str:
        return f"{self.name} ({self.height}cm, {self.age} days)"

    def get_height(self) -> int:
        return self.height

    def get_age(self) -> int:
        return self.age

    def get_name(self) -> str:
        return self.name

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print(
                f"[{self.get_name()}] Invalid operation attempted:"
                f"height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected.")
        else:
            self.height = new_height
            print(f"[{self.get_name()}] Height updated: {self.height}cm [OK]")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(
                f"[{self.get_name()}] Invalid operation attempted: "
                f"age {new_age} days [REJECTED]")
            print("Security: Negative age rejected.")
        else:
            self.age = new_age
            print(f"[{self.get_name()}] Age updated: {self.age} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Lotus", 42, 20),
        Plant("Fern", 15, 120)
    ]
    print()
    plants[0].set_height(25)
    print()
    plants[1].set_height(-5)
    print()
    plants[1].set_age(25)
    for plant in plants:
        print(f"Current plant: {plant.get_info()}")
