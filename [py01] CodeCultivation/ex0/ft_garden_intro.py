#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_intro.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/14 22:25:05 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/15 20:22:32 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_garden_intro(name: str, height: str, age: str) -> None:
    """Print the introduction of garden."""
    print("=== Welcome to My Garden ===")
    print("Name: " + name)
    print("Height: " + height + " cm")
    print("Age: " + age + " days")

if __name__ == "__main__":
    name = "Rose";
    height = "25";
    age = "30";
    ft_garden_intro(name, height, age)
    print("\n=== End of Program ===")
