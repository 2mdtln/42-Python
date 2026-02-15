#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_data.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/14 23:24:35 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/15 19:55:49 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    """Plant class to store the data of garden."""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
