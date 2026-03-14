# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_vault_security.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/14 11:39:15 by mtaheri            #+#    #+#             #
#   Updated: 2026/03/14 13:00:13 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def main() -> None:
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    try:
        with open("classified_data.txt") as f:
            print(f.read())
    except Exception as e:
        print(f"ERROR: {e}")
        return

    print("\nSECURE PRESERVATION:")
    try:
        with open("security_protocols.txt") as f:
            f_content = f.read()
            print(f_content)
            with open("classified_data.txt", "a") as f1:
                f1.write(f"\n{f_content}")
    except Exception as e:
        print(f"ERROR: {e}")
        return
    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    main()
