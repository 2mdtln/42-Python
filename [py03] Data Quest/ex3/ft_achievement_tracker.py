# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_achievement_tracker.py                           :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/26 16:32:52 by mtaheri            #+#    #+#             #
#   Updated: 2026/03/03 22:32:34 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Player:
    def __init__(self, name: str, achievements: set) -> None:
        self.name = name
        self.achievements = achievements

    def get_achievements(self) -> set:
        return self.achievements


def main():
    print("=== Achievement Tracker System ===")
    print()
    players = [
        Player("alice", {"first_kill", "level_10", "treasure_hunter",
               "speed_demon"}),
        Player("bob", {"first_kill", "level_10", "boss_slayer", "collector"}),
        Player("charlie", {"level_10", "treasure_hunter", "boss_slayer",
               "speed_demon", "perfectionist"})
    ]

    for player in players:
        print(f"Player {player.name} achievements:", player.get_achievements())
    print("\n=== Achievement Analytics ===")
    all_achievements = set()
    for player in players:
        all_achievements = all_achievements.union(player.get_achievements())
    print("All unique achievements:", all_achievements)
    print("Total unique achievements:", len(all_achievements))

    common = players[0].get_achievements()
    for player in players[1:]:
        common = common.intersection(player.get_achievements())
    print("\nCommon to all players:", common)
    rare = set()
    for achievement in all_achievements:
        count = 0
        for player in players:
            if achievement in player.get_achievements():
                count += 1
        if count == 1:
            rare = rare.union({achievement})
    print("Rare achievements (1 player):", rare)

    alice = players[0]
    bob = players[1]
    print("\nAlice vs Bob common:",
          alice.get_achievements().intersection(bob.get_achievements()))
    print("Alice unique:",
          alice.get_achievements().difference(bob.get_achievements()))
    print("Bob unique:",
          bob.get_achievements().difference(alice.get_achievements()))


if __name__ == "__main__":
    main()
