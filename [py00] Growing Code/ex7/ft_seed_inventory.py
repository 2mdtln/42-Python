# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_seed_inventory.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/13 17:31:01 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/19 20:13:20 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #


def last_part(quantity: int, unit: str) -> str:
    if (unit == "packets"):
        return (f"{quantity} packets available")
    elif (unit == "grams"):
        return (f"{quantity} grams total")
    elif (unit == "area"):
        return (f"covers {quantity} square meters")

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit == "packets" or unit == "grams" or  unit == "area"):
        print(f"{seed_type.capitalize()} seeds: {last_part(quantity, unit)}")
    else:
        print("Unknown unit type")
