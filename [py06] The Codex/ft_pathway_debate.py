# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_pathway_debate.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/29 17:05:15 by mtaheri            #+#    #+#             #
#   Updated: 2026/03/29 17:10:19 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #


import alchemy.transmutation
from alchemy.transmutation.advanced import elixir_of_life, philosophers_stone
from alchemy.transmutation.basic import lead_to_gold, stone_to_gem


def main() -> None:
    print("=== Pathway Debate Mastery ===")

    print("\nTesting Absolute Imports (from basic.py):")
    print("lead_to_gold():", lead_to_gold())
    print("stone_to_gem():", stone_to_gem())

    print("\nTesting Relative Imports (from advanced.py):")
    print("philosophers_stone():", philosophers_stone())
    print("elixir_of_life():", elixir_of_life())

    print("\nTesting Package Access:")
    print("alchemy.transmutation.lead_to_gold():",
          alchemy.transmutation.lead_to_gold())
    print("alchemy.transmutation.philosophers_stone():",
          alchemy.transmutation.philosophers_stone())

    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
