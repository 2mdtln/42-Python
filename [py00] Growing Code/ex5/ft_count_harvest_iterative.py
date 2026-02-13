# **************************************************************************** #
#                                                                              #
#                                                          :::      ::::::::   #
#   ft_count_harvest_iterative.py                        :+:      :+:    :+:   #
#                                                      +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr>  +#+  +:+       +#+        #
#                                                  +#+#+#+#+#+   +#+           #
#   Created: 2026/02/13 15:44:20 by mtaheri             #+#    #+#             #
#   Updated: 2026/02/13 18:46:48 by mtaheri            ###   ########.fr       #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    days_until = int(input("Days until harvest: "))
    for i in range(1, days_until):
        print("Day", i)
    print("Harvest time!")
