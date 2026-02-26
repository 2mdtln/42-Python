# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_coordinate_system.py                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/26 12:47:20 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/26 14:57:01 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import math


def distance(pos1: int, pos2: int) -> float:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


def parse_and_distance(pos_str: , distance_from) -> None:
    try:
        x, y, z = map(int, pos_str.split(","))
        print(f"Parsed position: {(x, y, z)}")
        print(f"Distance between {distance_from} "
              f"and {(x, y, z)}: {distance((x, y, z), distance_from):.1f}\n")
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print("Error details - "
              f"Type: {e.__class__.__name__}, Args: (\"{e}\",)")


def main():
    pos = tuple((10, 20, 5))
    spawn_point = tuple((0, 0, 0))
    print(f"Position created: {pos}")
    print(f"Distance between {spawn_point} and "
          f"{pos}: {distance(pos, spawn_point):.2f}\n")
    parse_pos = "3,4,0"
    print(f"Parsing coordinates: {parse_pos}")
    parse_and_distance(parse_pos, spawn_point)
    parse_pos = "3,one,0"
    print(f"Parsing invalid coordinates: \"{parse_pos}\"")
    parse_and_distance(parse_pos, spawn_point)
    print("\nUnpacking demonstration:")
    x, y, z = pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: x={x}, y={y}, z={z}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    main()
