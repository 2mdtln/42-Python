# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_raise_errors.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/23 17:46:18 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/27 07:38:53 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def check_plant_health(plant_name: str, water_level: float,
                       sunlight_hours: float) -> None:
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         f"is too high (max 12)")
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    print("\nTesting good values...")
    try:
        check_plant_health("Cherry", 1, 6)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 1, 6)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting bad water level...")
    try:
        check_plant_health("Rose", 15, 6)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("Sunflower", 1, 0)
    except ValueError as e:
        print(f"Error: {e}")
    

if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")
    test_plant_checks()
    print("\nAll error raising tests completed!")
