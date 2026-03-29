# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   validator.py                                        :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/29 17:15:28 by mtaheri            #+#    #+#             #
#   Updated: 2026/03/29 17:21:01 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def validate_ingredients(ingredients: str) -> str:
    is_valid = any(element in ingredients.lower() for
                   element in ["fire", "water", "earth", "air"])
    return f"{ingredients} - {"VALID" if is_valid else "INVALID"}"
