# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_crisis_response.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/14 12:06:18 by mtaheri            #+#    #+#             #
#   Updated: 2026/03/14 12:48:23 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #


def open_file(file_name: str, exception_type: Exception,
              access_msg: str, error_msg: str = "err",
              status_msg: str = "Normal operations resumed") -> None:
    print(f"{access_msg} '{file_name}'...")
    try:
        with open(file_name) as f:
            print(f"SUCCESS: Archive recovered - ``{f.read()}''")
    except exception_type or Exception:
        print(f"RESPONSE: {error_msg}")
    print(f"STATUS: {status_msg}\n")


def main() -> None:
    arcs = ["lost_archive.txt", "classified_vault.txt", "standard_archive.txt"]

    open_file(arcs[0], FileNotFoundError,
              "CRISIS ALERT: Attempting access to",
              "Archive not found in storage matrix",
              "Crisis handled, system stable")

    open_file(arcs[1], PermissionError,
              "CRISIS ALERT: Attempting access to",
              "Security protocols deny access",
              "Crisis handled, security maintained")

    open_file(arcs[2], Exception,
              "ROUTINE ACCESS: Attempting access to")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    main()
