# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_water_reminder.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/12 19:34:51 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/19 18:47:46 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_water_reminder() -> None:
    days = int(input("Days since last watering: "))
    if (days > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
