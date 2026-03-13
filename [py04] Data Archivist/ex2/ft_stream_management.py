# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_stream_management.py                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/13 21:25:47 by mtaheri            #+#    #+#             #
#   Updated: 2026/03/13 22:31:54 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import sys


def ft_input(prompt: str) -> str:
    print(prompt, end="", flush=True)
    input_str = sys.stdin.readline()
    if not input_str:
        sys.stderr.write("\nERROR: stdin empty\n")
        sys.exit(1)
    if input_str[-1] == '\n':
        input_str = input_str[:-1]
    else:
        sys.stdout.write("\n")
    return input_str


def main() -> None:
    archivist_id = ft_input("Input Stream active. Enter archivist ID: ")
    archivist_report = ft_input("Input Stream active. Enter status report: ")

    sys.stdout.write(f"\n[STANDARD] Archive status from "
                     f"{archivist_id}: {archivist_report}\n")
    sys.stdout.flush()
    sys.stderr.write("[ALERT] System diagnostic: "
                     "Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    main()
