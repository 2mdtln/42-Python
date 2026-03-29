# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_sacred_scroll.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/29 13:00:35 by mtaheri            #+#    #+#             #
#   Updated: 2026/03/29 13:49:34 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import alchemy
import alchemy.elements

print("=== Sacred Scroll Mastery ===")

print("\nTesting direct module access:")
print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
print(f"alchemy.elements.create_water(): {alchemy.elements.create_water()}")
print(f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}")
print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")

print("\nTesting package-level access (controlled by __init__.py):")
for name in ["create_fire", "create_water", "create_earth", "create_air"]:
    try:
        result = getattr(alchemy, name)()
        print(f"alchemy.{name}(): {result}")
    except AttributeError:
        print(f"alchemy.{name}(): AttributeError - not exposed")

print("\nPackage metadata:")
print(f"Version: {alchemy.__version__}")
print(f"Author: {alchemy.__author__}")
