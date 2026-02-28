# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_management.py                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/23 18:13:37 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/28 10:19:25 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__water_level = 0
        self.__sun_level = 1

    def get_name(self) -> str:
        return self.__name

    def water(self) -> None:
        self.__water_level += 4.2
        print(f"Watering {self.__name} - success")

    def get_water_level(self) -> float:
        return self.__water_level

    def sun(self) -> None:
        self.__sun_level += 1.25

    def get_sun_level(self) -> float:
        return self.__sun_level

    def check_plant_health(self) -> None:
        if not self.__name:
            raise PlantError("Plant name cannot be empty!")
        elif self.__water_level > 10:
            raise PlantError(f"Water level {self.__water_level}"
                                   f" is too high (max 10)")
        elif self.__water_level < 1:
            raise PlantError(f"Water level {self.__water_level}"
                                   f" is too low (min 1)")
        elif self.__sun_level < 2:
            raise PlantError(f"Sunlight hours {self.__sun_level}"
                                   f" is too low (min 2)")
        elif self.__sun_level > 12:
            raise PlantError(f"Sunlight hours {self.__sun_level} "
                                   f"is too high (max 12)")
        else:
            print(f"{self.__name}: healthy (water: "
                  f"{self.__water_level}, sun: {self.__sun_level})")


class GardenManager:
    _plants = []
    _is_watering = False
    _tank = 20

    @classmethod
    def add_plant(cls, plant: Plant) -> None:
        if not plant.get_name():
            raise PlantError("Plant name cannot be empty!")
        cls._plants = cls._plants + [plant]
        print(f"Added {plant.get_name()} successfully")

    @classmethod
    def start_watering_system(cls) -> None:
        cls._is_watering = True
        print("Opening watering system")

    @classmethod
    def stop_watering_system(cls) -> None:
        cls._is_watering = False
        print("Closing watering system (cleanup)")

    @classmethod
    def water_plants(cls) -> None:
        for plant in cls._plants:
            plant.sun()
            if cls._is_watering:
                if cls._tank - 4.2 < 0:
                    raise WaterError("Not enough water in tank!")
                cls._tank -= 4.2
                plant.water()

    @classmethod
    def get_plants(cls) -> list:
        return cls._plants


def test_garden_management(plants: Plant) -> None:
    print("\nAdding plants to garden...")
    for plant in plants:
        try:
            GardenManager.add_plant(plant)
        except PlantError as e:
            print(f"Error adding plant: {e}")
    print("\nWatering plants...")
    try:
        GardenManager.start_watering_system()
        for _ in range(1):
            GardenManager.water_plants()
    except GardenError as e:
        print(f"Error watering plants: {e}")
    finally:
        GardenManager.stop_watering_system()
    print("\nChecking plant health...")
    for plant in GardenManager.get_plants():
        try:
            plant.check_plant_health()
        except PlantError as e:
            print(f"Error checking {plant.get_name()}: {e}")
    print("\nTesting error recovery...")
    try:
        GardenManager.start_watering_system()
        GardenManager.water_plants()
    except GardenError as e:
        print(f"Error watering plants: {e}")
    finally:
        GardenManager.stop_watering_system()
    print("System recovered and continuing...")
    

if __name__ == "__main__":
    print("=== Garden Management System ===")
    plants = [Plant("Rose"), Plant("Cherry"), Plant("Lotus"), Plant("")]
    test_garden_management(plants)
    print("\nGarden management system test complete!")
