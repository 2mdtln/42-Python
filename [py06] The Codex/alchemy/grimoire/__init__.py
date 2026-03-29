# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   __init__.py                                         :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/29 17:14:54 by mtaheri            #+#    #+#             #
#   Updated: 2026/03/29 17:18:52 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from .spellbook import record_spell
from .validator import validate_ingredients

__all__ = ["record_spell", "validate_ingredients"]
