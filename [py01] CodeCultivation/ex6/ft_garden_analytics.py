#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_analytics.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/16 19:03:50 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/16 23:08:34 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self, amount: int = 1) -> None:
        self.height += amount
        print(f"{self.name} grew {amount}cm")

    def get_info(self) -> str:
        return (f"{self.name}: {self.height}cm")

    def get_type_name(self) -> str:
        return ("regular")

    def get_score(self) -> int:
        return (self.height)


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def get_info(self) -> str:
        state = "blooming" if self.is_blooming else "not blooming"
        return (f"{self.name}: {self.height}cm, "
                f"{self.color} flowers ({state})")

    def get_type_name(self) -> str:
        return ("flowering")

    def get_score(self) -> int:
        bonus = 3 if self.is_blooming else 0
        return (self.height + bonus)


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        color: str,
        prize_points: int,
    ) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self) -> str:
        base = super().get_info()
        return (f"{base}, Prize points: {self.prize_points}")

    def get_type_name(self) -> str:
        return ("prize")

    def get_score(self) -> int:
        base = super().get_score()
        return (base + self.prize_points)


class GardenManager:
    total_gardens = 0

    class GardenStats:
        def __init__(self) -> None:
            self.plants_added = 0
            self.total_growth = 0

        def record_plant_added(self) -> None:
            self.plants_added += 1

        def record_growth(self, amount: int) -> None:
            self.total_growth += amount

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants: list[Plant] = []
        self.stats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants = self.plants + [plant]
        self.stats.record_plant_added()
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_all_plants_grow(self, amount: int = 1) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)
            self.stats.record_growth(amount)

    def plant_type_counts(self) -> tuple[int, int, int]:
        regular = 0
        flowering = 0
        prize = 0
        for plant in self.plants:
            plant_type = plant.get_type_name()
            if plant_type == "regular":
                regular += 1
            elif plant_type == "flowering":
                flowering += 1
            else:
                prize += 1
        return (regular, flowering, prize)

    def garden_score(self) -> int:
        score = 0
        for plant in self.plants:
            score += plant.get_score()
        return (score)

    def report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")
        (regular, flowering, prize) = self.plant_type_counts()
        print(
            f"Plants added: {self.stats.plants_added}, "
            f"Total growth: {self.stats.total_growth}cm")
        print(
            f"Plant types: {regular} regular, {flowering} flowering, "
            f"{prize} prize flowers")

    @classmethod
    def create_garden_network(cls) -> None:
        print(f"Total gardens managed: {cls.total_gardens}")

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    mtaheri = GardenManager("mtaheri")
    bot1 = GardenManager("bot1")
    cherry = Plant("cherry Tree", 100)
    lotus = FloweringPlant("lotus", 25, "pink")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    lotus.bloom()
    mtaheri.add_plant(cherry)
    mtaheri.add_plant(lotus)
    mtaheri.add_plant(sunflower)
    mtaheri.help_all_plants_grow()
    mtaheri.report()
    print(f"Height validation test: {GardenManager.validate_height(10)}")
    bot1.add_plant(Plant("Pine Tree", 90))
    bot1.help_all_plants_grow()
    print(f"Garden scores - mtaheri: {mtaheri.garden_score()}, "
          f"bot1: {bot1.garden_score()}")
    GardenManager.create_garden_network()
