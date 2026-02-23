# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_first_exception.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/18 11:37:19 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/23 17:49:39 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def check_temperature(temp_str: str) -> None:
    try:
        temp = int(temp_str)
        if temp > 0 and temp < 40:
            print(f"Temperature {temp}°C is perfect for plants!")
        if temp <= 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        if temp >= 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print()
    print("Testing temperature: 25")
    check_temperature("25")
    print()
    print("Testing temperature: abc")
    check_temperature("abc")
    print()
    print("Testing temperature: 100")
    check_temperature("100")
    print()
    print("Testing temperature: -50")
    check_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")
