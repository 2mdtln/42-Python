# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_archive_creation.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/13 20:49:59 by mtaheri            #+#    #+#             #
#   Updated: 2026/03/13 21:24:40 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def main() -> None:
    file_name = "new_discovery.txt"
    content_to_write = ("[ENTRY 001] New quantum algorithm discovered\n"
                        "[ENTRY 002] Efficiency increased by 347%\n"
                        "[ENTRY 003] Archived by Data Archivist trainee")
    print(f"Initializing new storage unit: {file_name}")

    try:
        file = open(file_name, "x")
    except FileExistsError:
        print("ERROR: file exists")
        return
    print("Storage unit created successfully...\n\n"
          "Inscribing preservation data...")

    try:
        file.writelines(content_to_write)
        print(content_to_write)
    except Exception as e:
        print(f"ERROR: {e}")

    file.close()
    print("\nData inscription complete. Storage unit sealed.\n"
          f"Archive '{file_name}' ready for long-term preservation")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    main()
