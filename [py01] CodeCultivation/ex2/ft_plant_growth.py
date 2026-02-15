#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plant_growth.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/15 19:49:25 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/15 20:20:36 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    """Plant class to store the data of garden."""
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, growth: int) -> None:
        """grow the plant (increase height)."""
        self.height += growth

    def age(self, days: int) -> None:
        """age the plant (increase age)."""
        self.age += days

    def get_info(self) -> str:
        """get the information of plant."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    lotus = Plant("Lotus", 40, 20)
    rose_height = rose.height
    lotus_height = lotus.height
    print("=== Day 1 ===")
    print(rose.get_info())
    print(rose.get_info())
    rose.grow(5)
    rose.age(6)
    lotus.grow(10)
    lotus.age(6)
    print("=== Day 7 ===")
    print(get_info(rose))
    print(get_info(lotus))
    print(f"{rose.name}: Growth this week: +{rose.height - rose_height}cm")
    print(f"{lotus.name}: Growth this week: +{lotus.height - lotus_height}cm")
