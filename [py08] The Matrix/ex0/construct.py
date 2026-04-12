# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   construct.py                                        :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/11 19:35:35 by mtaheri            #+#    #+#             #
#   Updated: 2026/04/12 12:50:31 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import sys
import os
import site


def main() -> None:
    venv = os.environ.get("VIRTUAL_ENV")

    if venv:
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(venv)}")
        print(f"Environment Path: {venv}\n")
        print("\033[32mSUCCESS: You're in an isolated environment!\033[0m\n")

        print("Package installation path:\n",
              site.getsitepackages()[0]
              if hasattr(site, "getsitepackages") else "")
    else:
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")

        print("\033[33mWARNING: You're in the global environment!\033[0m\n")

        print("To create a virtual environment, run:")
        print(" python -m venv .venv\n")
        print(" source .venv/bin/activate   # Mac/Linux")
        print(" .venv\\Scripts\\activate      # Microslop Windows\n")
        print(" deactivate                  # to deactivate\n")

        print("Then run this program again.")


if __name__ == "__main__":
    main()
