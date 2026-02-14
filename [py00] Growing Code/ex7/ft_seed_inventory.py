# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_seed_inventory.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/13 17:31:01 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/14 20:38:04 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    is_area = False
    if unit == "packets":
        final_unit = "packets available"
    elif unit == "grams":
        final_unit = "grams total"
    elif unit == "area":
        final_unit = "square meters"
        is_area = True
    else:
        final_unit = "Unknown unit type"
    prefix = "covers " if is_area else ""
    print(f"{seed_type} seeds: {prefix}{quantity} {final_unit}")
