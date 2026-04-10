# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   tournament.py                                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/09 18:25:54 by mtaheri            #+#    #+#             #
#   Updated: 2026/04/09 18:59:10 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (AggressiveStrategy, BattleStrategy,
                 DefensiveStrategy, InvalidStrategyError,
                 NormalStrategy)

Opponent = tuple[CreatureFactory, BattleStrategy]


def strategy_name(strategy: BattleStrategy) -> str:
    if isinstance(strategy, NormalStrategy):
        return "Normal"
    if isinstance(strategy, AggressiveStrategy):
        return "Aggressive"
    return "Defensive"


def opponent_name(factory: CreatureFactory) -> str:
    creature = factory.create_base()
    if creature.name in ("Sproutling", "Bloomelle"):
        return "Healing"
    if creature.name in ("Shiftling", "Morphagon"):
        return "Transform"
    return creature.name


def display_opponents(opponents: list[Opponent]) -> None:
    labels: list[str] = []
    for factory, strategy in opponents:
        labels.append(f"({opponent_name(factory)}+{strategy_name(strategy)})")
    print("[ " + ", ".join(labels) + " ]")


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    try:
        for first_index in range(len(opponents)):
            for second_index in range(first_index + 1, len(opponents)):
                first_factory, first_strategy = opponents[first_index]
                second_factory, second_strategy = opponents[second_index]
                first_creature = first_factory.create_base()
                second_creature = second_factory.create_base()
                print("\n* Battle *")
                print(first_creature.describe())
                print(" vs.")
                print(second_creature.describe())
                print(" now fight!")
                for action in first_strategy.act(first_creature):
                    print(action)
                for action in second_strategy.act(second_creature):
                    print(action)
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


def main() -> None:
    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()
    tournament_zero: list[Opponent] = [
        (FlameFactory(), normal_strategy),
        (HealingCreatureFactory(), defensive_strategy),
    ]
    tournament_one: list[Opponent] = [
        (FlameFactory(), aggressive_strategy),
        (HealingCreatureFactory(), defensive_strategy),
    ]
    tournament_two: list[Opponent] = [
        (AquaFactory(), normal_strategy),
        (HealingCreatureFactory(), defensive_strategy),
        (TransformCreatureFactory(), aggressive_strategy),
    ]

    print("Tournament 0 (basic)")
    display_opponents(tournament_zero)
    battle(tournament_zero)

    print("\nTournament 1 (error)")
    display_opponents(tournament_one)
    battle(tournament_one)

    print("\nTournament 2 (multiple)")
    display_opponents(tournament_two)
    battle(tournament_two)


if __name__ == "__main__":
    main()
