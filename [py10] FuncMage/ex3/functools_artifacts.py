# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   functools_artifacts.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/16 00:39:37 by mtaheri            #+#    #+#             #
#   Updated: 2026/04/16 20:24:26 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import functools
import operator
from typing import Any, Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    ops = {"add": operator.add,
           "multiply": operator.mul,
           "max": lambda a, b: a if a > b else b,
           "min": lambda a, b: a if a < b else b}
    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "mending": functools.partial(base_enchantment,
                                     power=50, book="mending"),
        "sharpness": functools.partial(base_enchantment,
                                       power=50, book="sharpness"),
        "unbreaking": functools.partial(base_enchantment,
                                        power=50, book="unbreaking")}


def apply_enchantment(weapon, power, book):
    return f"{weapon} enchanted with {book} (power: {power})"


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatch(spell) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f" Sum: {spell_reducer(spells, 'add')}")
    print(f" Product: {spell_reducer(spells, 'multiply')}")
    print(f" Max: {spell_reducer(spells, 'max')}")

    print("\nTesting enchantments:")
    enchantments = partial_enchanter(apply_enchantment)
    for element in enchantments:
        result = enchantments[element]("sword")
        print(f"  {element}: {result}")
    print("Testing mending enchantment:")
    result = enchantments["mending"]("elytra")
    print(f"   Result: {result}\n")

    print("\nTesting memoized fibonacci...")
    print(f" Fib(0): {memoized_fibonacci(0)}")
    print(f" Fib(1): {memoized_fibonacci(1)}")
    print(f" Fib(10): {memoized_fibonacci(10)}")
    print(f" Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(f" {dispatch(42)}")
    print(f" {dispatch("mending")}")
    print(f" {dispatch([1, 2, 3])}")
    print(f" {dispatch(3.14)}")
