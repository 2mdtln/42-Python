#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plant_factory.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/16 12:10:01 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/16 19:14:29 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    plant_count = 0

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        Plant.plant_count += 1

    def get_info(self) -> str:
        return f"{self.name} ({self.height}cm, {self.age} days)"


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 90, 50),
        Plant("Lotus", 42, 20),
        Plant("Fern", 15, 120)
    ]
    for plant in plants:
        print(f"Created: {plant.get_info()}")
    print(f"\nTotal plants created: {Plant.plant_count}")
