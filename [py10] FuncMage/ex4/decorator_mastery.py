# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   decorator_mastery.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/16 00:39:39 by mtaheri            #+#    #+#             #
#   Updated: 2026/04/16 20:22:16 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import functools
import time
from typing import Callable


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(power, *args, **kwargs):
            if power < min_power:
                return "Insufficient power"
            return func(power, *args, **kwargs)
        return wrapper
    return decorator


@power_validator(min_power=30)
def spawn(power, name):
    return f"{name} spawned w/ {power} power points"


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c == " " for c in name)

    def cast_spell(self, spell_name: str, power: int) -> str:
        @power_validator(min_power=10)
        def _cast(power: int, spell_name: str) -> str:
            return f"Successfully cast {spell_name} with {power} power"
        return _cast(power, spell_name)


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting spawn (min 30 power):")
    print(f"  Power 20: {spawn(20, 'goblin')}")
    print(f"  Power 42: {spawn(42, 'goblin')}")

    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def failing_spell():
        raise RuntimeError("nope")
    print(failing_spell())
    print("Waaaaaaagh spelled!")

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("random name"))
    print(MageGuild.validate_mage_name("xs"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
