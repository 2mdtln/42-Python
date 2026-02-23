# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_custom_errors.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/21 22:17:40 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/23 17:49:00 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, status: str) -> None:
        self.__name = name
        self.__status = status

    def get_status(self):
        return self.__status

    def get_name(self):
        return self.__name

    def set_status(self, status: str):
        self.__status = status
        if self.__status == "wilting":
            raise PlantError(f"The {self.__name} plant is wilting!")


def check_water(amount: int) -> None:
    if amount < 0:
        raise WaterError("Water amount cannot be negative!")
    elif amount < 50:
        raise WaterError("Not enough water in the tank!")
    elif amount > 200:
        raise WaterError("Too much water!")
    else:
        print("Water amount is just right!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        lotus = Plant("Lotus", "healthy")
        lotus.set_status("wilting")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("\nTesting WaterError...")
    try:
        check_water(42)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\nTesting catching all garden errors...")
    try:
        lotus.set_status("wilting")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        check_water(42)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")
