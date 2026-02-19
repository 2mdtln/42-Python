# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_count_harvest_recursive.py                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/13 15:44:29 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/19 18:47:57 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def loop(day: int) -> None:
    if day == 0:
        return
    loop(day - 1)
    print("Day", day)


def ft_count_harvest_recursive() -> None:
    days_until = int(input("Days until harvest: "))
    loop(days_until)
    print("Harvest time!")
