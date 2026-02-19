# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_summary.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/02/13 17:23:42 by mtaheri            #+#    #+#             #
#   Updated: 2026/02/19 18:48:00 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_garden_summary() -> None:
    name = input("Enter garden name: ")
    num_of_plants = input("Enter number of plants: ")
    print("Garden:", name)
    print("Plants:", num_of_plants)
    print("Status: Growing well!")
