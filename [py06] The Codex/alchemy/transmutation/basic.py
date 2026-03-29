# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   basic.py                                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/29 16:58:39 by mtaheri            #+#    #+#             #
#   Updated: 2026/03/29 17:05:09 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #


from alchemy.elements import create_earth, create_fire


def lead_to_gold() -> str:
    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem() -> str:
    return f"Stone transmuted to gem using {create_earth()}"
