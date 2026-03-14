# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_crisis_response.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/14 12:06:18 by mtaheri            #+#    #+#             #
#   Updated: 2026/03/14 13:12:10 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def open_file(file_name: str, access_msg: str) -> None:
    print(f"{access_msg} '{file_name}'...")
    try:
        with open(file_name) as file:
            print(f"SUCCESS: Archive recovered - ``{file.read()}''")
            print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception:
        print("RESPONSE: Unexpected error")
        print("STATUS: Crisis handled.\n")


def main() -> None:
    arcs = ["lost_archive.txt", "classified_vault.txt", "standard_archive.txt"]

    open_file(arcs[0], "CRISIS ALERT: Attempting access to")
    open_file(arcs[1], "CRISIS ALERT: Attempting access to")
    open_file(arcs[2], "ROUTINE ACCESS: Attempting access to")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    main()
