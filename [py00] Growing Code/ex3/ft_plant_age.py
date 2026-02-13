# **************************************************************************** #
#                                                                              #
#                                                          :::      ::::::::   #
#   ft_plant_age.py                                      :+:      :+:    :+:   #
#                                                      +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr>  +#+  +:+       +#+        #
#                                                  +#+#+#+#+#+   +#+           #
#   Created: 2026/02/12 19:13:27 by mtaheri             #+#    #+#             #
#   Updated: 2026/02/13 18:45:26 by mtaheri            ###   ########.fr       #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    days = int(input("Enter plant age in days: "))
    if (days > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
