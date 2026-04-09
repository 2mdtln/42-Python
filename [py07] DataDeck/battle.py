# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   battle.py                                           :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/08 20:21:07 by mtaheri            #+#    #+#             #
#   Updated: 2026/04/09 17:16:28 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    base_creature = factory.create_base()
    evolved_creature = factory.create_evolved()
    print("Testing factory")
    print(base_creature.describe())
    print(base_creature.attack())
    print(evolved_creature.describe())
    print(evolved_creature.attack())
    print()


def battle_base_creatures(
                          first_factory: CreatureFactory,
                          second_factory: CreatureFactory) -> None:
    first_creature = first_factory.create_base()
    second_creature = second_factory.create_base()
    print("Testing battle")
    print(first_creature.describe())
    print(" vs.")
    print(second_creature.describe())
    print(" fight!")
    print(first_creature.attack())
    print(second_creature.attack())


def main() -> None:
    try:
        flame_factory = FlameFactory()
        aqua_factory = AquaFactory()
        test_factory(flame_factory)
        test_factory(aqua_factory)
        battle_base_creatures(flame_factory, aqua_factory)
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
