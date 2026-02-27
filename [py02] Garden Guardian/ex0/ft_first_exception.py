# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_first_exception.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/18 11:37:19 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/27 07:47:10 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def check_temperature(temp_str: str) -> None:
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(f"'{temp_str}' is not a valid number")
        return
    if temp > 0 and temp < 40:
        print(f"Temperature {temp}°C is perfect for plants!")
    if temp <= 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp >= 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")


def test_error_types() -> None:
    tests = ["25", "abc", "100", "-50"]
    for test in tests:
        try:
            print()
            print(f"Testing temperature: {test}")
            check_temperature(test)
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_error_types()
    print()
    print("All tests completed - program didn't crash!")
