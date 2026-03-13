# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_ancient_text.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/13 20:31:34 by mtaheri            #+#    #+#             #
#   Updated: 2026/03/13 20:49:22 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def main() -> None:
    file_name = "ancient_fragment.txt"

    print(f"Accessing Storage Vault: {file_name}")
    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
        return

    try:
        file_content = file.read()
    except Exception as e:
        print(f"ERROR: {e}")
        return
    print("Connection established...\n")
    print("RECOVERED DATA:")
    if not file_content:
        print("--- file empty ---")
    else:
        print(file_content)

    file.close()
    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    main()
