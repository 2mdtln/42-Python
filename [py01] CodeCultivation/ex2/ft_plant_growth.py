#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plant_growth.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/15 19:49:25 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/16 19:13:45 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def grow(self, growth: int) -> None:
        self.height += growth

    def increase_age(self, days: int) -> None:
        self.age += days

    def daily_growth(self, grow_amount: int) -> None:
        self.grow(grow_amount)
        self.increase_age(1)


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    lotus = Plant("Lotus", 40, 20)
    rose_height = rose.height
    lotus_height = lotus.height
    print("=== Day 1 ===")
    print(rose.get_info())
    print(lotus.get_info())
    for i in range(6):
        rose.daily_growth(1)
        lotus.daily_growth(2)
    print("=== Day 7 ===")
    print(rose.get_info())
    print(lotus.get_info())
    print(f"{rose.name}: Growth this week: +{rose.height - rose_height}cm")
    print(f"{lotus.name}: Growth this week: +{lotus.height - lotus_height}cm")
