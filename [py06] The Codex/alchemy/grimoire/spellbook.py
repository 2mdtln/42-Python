# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   spellbook.py                                        :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/29 17:15:26 by mtaheri            #+#    #+#             #
#   Updated: 2026/03/29 17:26:47 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    validation_result = validate_ingredients(ingredients)
    if validation_result.endswith(" - VALID"):
        return f"Spell recorded: {spell_name} ({validation_result})"
    return f"Spell rejected: {spell_name} ({validation_result})"
