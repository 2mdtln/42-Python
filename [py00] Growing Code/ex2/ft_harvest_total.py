# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_harvest_total.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/12 13:43:53 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/19 18:47:39 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_harvest_total() -> None:
    first_day = int(input("Day 1 harvest: "))
    second_day = int(input("Day 2 harvest: "))
    third_day = int(input("Day 3 harvest: "))
    print("Total harvest:", first_day + second_day + third_day)
