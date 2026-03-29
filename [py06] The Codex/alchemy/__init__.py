# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   __init__.py                                         :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/29 13:00:18 by mtaheri            #+#    #+#             #
#   Updated: 2026/03/29 13:48:58 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from .elements import create_fire, create_water

__version__ = "1.0.0"
__author__ = "Master Pythonicus"

__all__ = ["create_fire", "create_water"]
