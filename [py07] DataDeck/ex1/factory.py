# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   factory.py                                          :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/09 17:21:28 by mtaheri            #+#    #+#             #
#   Updated: 2026/04/09 18:06:58 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from ex0 import CreatureFactory
from ex0.creature import Creature
from .creature import Bloomelle, Morphagon, Shiftling, Sproutling


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
