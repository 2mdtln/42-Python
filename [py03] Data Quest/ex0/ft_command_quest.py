# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_command_quest.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/26 11:13:04 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/26 12:50:18 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import sys


def main() -> None:
    i = 0
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        print(f"Program name: {sys.argv[0]}")
        arguments = sys.argv[1:]
        print(f"Arguments received: {len(arguments)}")
        for arg in arguments:
            i += 1
            print(f"Argument {i}: {arg}")
    print(f"total arguments: {len(sys.argv)}\n")


if __name__ == "__main__":
    print("=== Command Quest ===")
    main()
