# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_score_analytics.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/26 11:55:51 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/26 12:50:03 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import sys


def main() -> None:
    arguments = []
    i = 0
    for arg in sys.argv[1:]:
        try:
            arguments = arguments + [int(arg)]
            i += 1
        except ValueError:
            print(f"oops, You typed {arg} instead of an int. (Skipping)")
    if len(arguments) == 0:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {arguments}")
        print(f"Total players: {i}")
        print(f"Total score: {sum(arguments)}")
        print(f"Average score: {sum(arguments) / i}")
        print(f"High score: {max(arguments)}")
        print(f"Low score: {min(arguments)}")
        print(f"Score range: {max(arguments) - min(arguments)}")
        print()


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    main()
