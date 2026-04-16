# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   higher_magic.py                                     :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/16 00:25:20 by mtaheri            #+#    #+#             #
#   Updated: 2026/04/16 16:55:07 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    def lightning(target: str, power: int) -> str:
        return f"Lightning strikes {target} for {power} damage"

    def ice_shard(target: str, power: int) -> str:
        return f"Ice Shard freezes {target} for {power} damage"

    def base_spell(target: str, power: int) -> str:
        return f"Spell hits {target} for {power} damage"

    print("Testing spell combiner...")
    result = spell_combiner(fireball, heal)("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    print(f"Original: {base_spell("test", 10)}\n"
          f"Amplified: {power_amplifier(base_spell, 3)("test", 10)}")

    print("\nTesting conditional caster...")
    strong_only = conditional_caster(lambda targ, pow: pow >= 20, fireball)
    print(strong_only("Dragon", 25))
    print(strong_only("Dragon", 5))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, lightning, ice_shard])
    for result in sequence("Titan", 15):
        print(result)
