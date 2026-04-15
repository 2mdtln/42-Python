# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   lambda_spells.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/15 22:32:09 by mtaheri            #+#    #+#             #
#   Updated: 2026/04/16 00:37:16 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        'max_power': max(mages, key=lambda m: m['power'])['power'],
        'min_power': min(mages, key=lambda m: m['power'])['power'],
        'avg_power': round(sum(map
                               (lambda m: m['power'], mages)) / len(mages), 2)}


if __name__ == "__main__":
    artifacts = [{'name': 'Storm Crown', 'power': 112, 'type': 'accessory'},
                 {'name': 'Storm Crown', 'power': 106, 'type': 'accessory'},
                 {'name': 'Light Prism', 'power': 106, 'type': 'relic'},
                 {'name': 'Water Chalice', 'power': 108, 'type': 'weapon'}]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    first, second = sorted_artifacts[0], sorted_artifacts[1]
    print(f"{first['name']} ({first['power']} power) "
          f"comes before {second['name']} ({second['power']} power)")

    spells = ['flash', 'earthquake', 'fireball', 'tornado']
    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))

    mages = [{'name': 'Ember', 'power': 90, 'element': 'lightning'},
             {'name': 'Ember', 'power': 72, 'element': 'ice'},
             {'name': 'Morgan', 'power': 70, 'element': 'light'},
             {'name': 'Phoenix', 'power': 67, 'element': 'light'},
             {'name': 'Sage', 'power': 85, 'element': 'shadow'}]
    print("\nTesting mage stats...")
    for key, val in mage_stats(mages).items():
        print(f"{key}: {val}")
