# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_finally_block.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/23 16:08:07 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/26 10:40:22 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__watered = False

    def get_name(self) -> str:
        return self.__name

    def water(self) -> None:
        self.__watered = True

    def is_watered(self) -> bool:
        return self.__watered


class InvalidPlantError(Exception):
    pass


class WateringSystemError(Exception):
    pass


class WateringSystem():
    def __init__(self) -> None:
        self._is_watering = False

    def start_watering(self) -> None:
        print("Opening watering system")
        self._is_watering = True

    def water_plants(self, plants: list) -> None:
        if not self._is_watering:
            raise WateringSystemError("Watering system is not started!")
        for plant in plants:
            if plant is None:
                raise InvalidPlantError("Cannot water None - invalid plant!")
            plant.water()
            print(f"Watering {plant.get_name()}")

    def stop_watering(self) -> None:
        print("Closing watering system (cleanup)")
        self._is_watering = False


def test_watering_system(plants: list, plants_bad: list,
                         WarningSystem: WateringSystem) -> None:
    print("\nTesting normal watering...")
    WarningSystem.start_watering()
    try:
        WarningSystem.water_plants(plants)
    except Exception as e:
        print(f"Caught an error: {e}")
    finally:
        WarningSystem.stop_watering()
    print("Watering completed successfully!")
    print("\nTesting with error...")
    WarningSystem.start_watering()
    try:
        WarningSystem.water_plants(plants_bad)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        WarningSystem.stop_watering()
    print("\nTesting with error...")
    WarningSystem = WateringSystem()
    try:
        WarningSystem.water_plants(plants)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        WarningSystem.stop_watering()


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    plants = [Plant("Rose"), Plant("Lotus"), Plant("Oak")]
    plants_bad = [Plant("Rose"), None, Plant("Oak")]
    WarningSystem = WateringSystem()
    test_watering_system(plants, plants_bad, WarningSystem)
    print("\nCleanup always happens, even with errors!")
