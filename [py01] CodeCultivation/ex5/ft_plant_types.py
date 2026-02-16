#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plant_types.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/16 16:47:57 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/16 22:27:13 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def get_info(self) -> str:
        return (f"{self.name} (Flower): {self.height}cm, "
                f"{self.age} days, {self.color} color")

    def bloom(self) -> None:
        self.is_blooming = True
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self) -> str:
        return (f"{self.name} (Tree): {self.height}cm, "
                f"{self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        print(f"{self.name} provides shade {self.trunk_diameter + 28} "
              f"square meters of shade.")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> str:
        return (f"{self.name} (Vegetable): {self.height}cm, "
                f"{self.age} days, {self.harvest_season} harvest"
                f"\n{self.name} is rich in {self.nutritional_value}.")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    lotus = Flower("Lotus", 42, 20, "pink")
    oak = Tree("Oak", 500, 1825, 50)
    cherry = Tree("Cherry", 150, 200, 30)
    tomato = Vegetable("Tomato", 50, 60, "summer", "vitamin C")
    cucumber = Vegetable("Cucumber", 30, 45, "summer", "hydration")
    plants = [rose, lotus, oak, cherry, tomato, cucumber]
    for plant in plants:
        print(plant.get_info())
    print()
    lotus.bloom()
    cherry.produce_shade()
