# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   advanced.py                                         :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/29 16:58:45 by mtaheri            #+#    #+#             #
#   Updated: 2026/03/29 17:10:36 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #


from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    return ("Philosopher's stone created using "
            f"{lead_to_gold()} and {healing_potion()}")


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
