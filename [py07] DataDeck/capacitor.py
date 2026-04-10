# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   capacitor.py                                        :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/09 17:19:02 by mtaheri            #+#    #+#             #
#   Updated: 2026/04/09 18:24:14 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from ex0.creature import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capability import HealCapability, TransformCapability


def show_healing_creature(creature: Creature) -> None:
    if not isinstance(creature, HealCapability):
        raise TypeError("Creature can't heal")
    print(creature.describe())
    print(creature.attack())
    print(creature.heal())


def test_healing_creature() -> None:
    factory = HealingCreatureFactory()
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()
    print("Testing Creature with healing capability")
    print(" base:")
    show_healing_creature(base_creature)
    print(" evolved:")
    show_healing_creature(evolved_creature)
    print()


def show_transform_creature(creature: Creature) -> None:
    if not isinstance(creature, TransformCapability):
        raise TypeError("Creature can't transform")
    print(creature.describe())
    print(creature.attack())
    print(creature.transform())
    print(creature.attack())
    print(creature.revert())


def test_transform_creature() -> None:
    factory = TransformCreatureFactory()
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()
    print("Testing Creature with transform capability")
    print(" base:")
    show_transform_creature(base_creature)
    print(" evolved:")
    show_transform_creature(evolved_creature)


def main() -> None:
    try:
        test_healing_creature()
        test_transform_creature()
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
